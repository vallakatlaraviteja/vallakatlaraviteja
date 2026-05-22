"""Liveness + readiness endpoints."""

from __future__ import annotations

import redis.asyncio as redis_async
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import Settings, get_settings
from app.db import get_session

router = APIRouter(tags=["health"])


@router.get("/healthz", summary="Liveness probe")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/readyz", summary="Readiness probe — checks DB + Redis")
async def readyz(
    session: AsyncSession = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> dict[str, str]:
    db_ok = False
    redis_ok = False
    try:
        await session.execute(text("SELECT 1"))
        db_ok = True
    except Exception:  # noqa: BLE001
        db_ok = False
    try:
        client = redis_async.from_url(settings.redis_url)
        await client.ping()
        await client.aclose()
        redis_ok = True
    except Exception:  # noqa: BLE001
        redis_ok = False
    return {
        "status": "ok" if (db_ok and redis_ok) else "degraded",
        "db": "ok" if db_ok else "down",
        "redis": "ok" if redis_ok else "down",
    }
