"""Event service — append-only audit + activity log."""

from __future__ import annotations

import uuid
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event import Event, EventKind


async def record_event(
    session: AsyncSession,
    *,
    candidate_id: uuid.UUID,
    kind: EventKind,
    summary: str,
    application_id: uuid.UUID | None = None,
    job_id: uuid.UUID | None = None,
    payload: dict[str, Any] | None = None,
) -> Event:
    event = Event(
        candidate_id=candidate_id,
        application_id=application_id,
        job_id=job_id,
        kind=kind,
        summary=summary,
        payload=payload or {},
    )
    session.add(event)
    await session.flush()
    return event
