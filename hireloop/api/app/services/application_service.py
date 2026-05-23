"""Application service — state machine, transitions, and event logging.

Centralizes the rules for how applications can move through the pipeline.
Pure-Python validation in `valid_transition` makes the state machine
unit-testable without a database.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.application import Application, ApplicationStatus
from app.models.event import EventKind
from app.models.job import Job
from app.services.event_service import record_event

# Allowed forward transitions. Rejected/withdrawn are reachable from any
# active stage. Accepted is terminal-positive; rejected/withdrawn terminal-negative.
_FORWARD: dict[ApplicationStatus, set[ApplicationStatus]] = {
    ApplicationStatus.saved: {ApplicationStatus.tailoring, ApplicationStatus.ready_to_apply, ApplicationStatus.applied},
    ApplicationStatus.tailoring: {ApplicationStatus.ready_to_apply, ApplicationStatus.applied},
    ApplicationStatus.ready_to_apply: {ApplicationStatus.applied},
    ApplicationStatus.applied: {ApplicationStatus.recruiter_screen},
    ApplicationStatus.recruiter_screen: {ApplicationStatus.tech_screen},
    ApplicationStatus.tech_screen: {ApplicationStatus.onsite},
    ApplicationStatus.onsite: {ApplicationStatus.offer},
    ApplicationStatus.offer: {ApplicationStatus.accepted},
    ApplicationStatus.accepted: set(),
    ApplicationStatus.rejected: set(),
    ApplicationStatus.withdrawn: set(),
}

_ACTIVE = {
    ApplicationStatus.saved,
    ApplicationStatus.tailoring,
    ApplicationStatus.ready_to_apply,
    ApplicationStatus.applied,
    ApplicationStatus.recruiter_screen,
    ApplicationStatus.tech_screen,
    ApplicationStatus.onsite,
    ApplicationStatus.offer,
}

# Status that timestamps `applied_at` automatically the first time we hit it.
_APPLIED_TIMESTAMP_TRIGGER = ApplicationStatus.applied



def valid_transition(current: ApplicationStatus, target: ApplicationStatus) -> bool:
    """Pure function: can `current` legally transition to `target`?"""
    if current == target:
        return True
    if target in {ApplicationStatus.rejected, ApplicationStatus.withdrawn}:
        return current in _ACTIVE
    return target in _FORWARD.get(current, set())


async def create_application(
    session: AsyncSession,
    *,
    candidate_id: uuid.UUID,
    job_id: uuid.UUID,
    notes_md: str | None = None,
    referrer_name: str | None = None,
    referrer_email: str | None = None,
) -> Application:
    job = await session.get(Job, job_id)
    if not job:
        raise ValueError(f"Job {job_id} not found")
    app_row = Application(
        candidate_id=candidate_id,
        job_id=job_id,
        status=ApplicationStatus.saved,
        notes_md=notes_md,
        referrer_name=referrer_name,
        referrer_email=referrer_email,
    )
    session.add(app_row)
    await session.flush()
    await record_event(
        session,
        candidate_id=candidate_id,
        application_id=app_row.id,
        job_id=job_id,
        kind=EventKind.application_created,
        summary=f"Saved {job.company} — {job.title}",
        payload={"company": job.company, "title": job.title},
    )
    return app_row



async def transition_status(
    session: AsyncSession,
    *,
    application: Application,
    target: ApplicationStatus,
) -> Application:
    """Apply a status transition with validation + event logging.

    Raises ValueError on illegal transitions (404/409 mapped at the router layer).
    """
    if not valid_transition(application.status, target):
        raise ValueError(
            f"Illegal transition: {application.status.value} -> {target.value}"
        )
    if application.status == target:
        return application
    previous = application.status
    application.status = target
    if target == _APPLIED_TIMESTAMP_TRIGGER and application.applied_at is None:
        application.applied_at = datetime.now(timezone.utc)
    await record_event(
        session,
        candidate_id=application.candidate_id,
        application_id=application.id,
        job_id=application.job_id,
        kind=EventKind.application_status_changed,
        summary=f"{previous.value} -> {target.value}",
        payload={"from": previous.value, "to": target.value},
    )
    return application


async def list_applications(
    session: AsyncSession,
    *,
    candidate_id: uuid.UUID,
    status: ApplicationStatus | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[Application]:
    stmt = (
        select(Application)
        .where(Application.candidate_id == candidate_id)
        .order_by(Application.updated_at.desc())
        .limit(limit)
        .offset(offset)
    )
    if status:
        stmt = stmt.where(Application.status == status)
    return list((await session.execute(stmt)).scalars().all())
