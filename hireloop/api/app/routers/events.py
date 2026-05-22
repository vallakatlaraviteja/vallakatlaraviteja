"""Read-only event log for the cockpit timeline."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import require_owner
from app.db import get_session
from app.models.event import Event, EventKind
from app.schemas.event import EventOut

router = APIRouter()


@router.get("", response_model=list[EventOut], summary="Recent events")
async def list_events(
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
    kind: EventKind | None = Query(None),
    application_id: uuid.UUID | None = Query(None),
    job_id: uuid.UUID | None = Query(None),
    limit: int = Query(100, ge=1, le=500),
) -> list[EventOut]:
    stmt = select(Event).order_by(Event.created_at.desc()).limit(limit)
    if kind:
        stmt = stmt.where(Event.kind == kind)
    if application_id:
        stmt = stmt.where(Event.application_id == application_id)
    if job_id:
        stmt = stmt.where(Event.job_id == job_id)
    rows = (await session.execute(stmt)).scalars().all()
    return [EventOut.model_validate(r) for r in rows]
