"""Candidate service — fetch / upsert the single owner row."""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateUpdate


async def get_owner(session: AsyncSession) -> Candidate | None:
    settings = get_settings()
    res = await session.execute(select(Candidate).where(Candidate.email == settings.owner_email))
    return res.scalar_one_or_none()


async def get_or_create_owner(session: AsyncSession) -> Candidate:
    settings = get_settings()
    row = await get_owner(session)
    if row:
        return row
    row = Candidate(
        email=settings.owner_email,
        full_name=settings.owner_name,
        constraints={},
        profile={},
    )
    session.add(row)
    await session.flush()
    return row


async def update_owner(session: AsyncSession, payload: CandidateUpdate) -> Candidate:
    row = await get_or_create_owner(session)
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(row, field, value)
    await session.flush()
    return row
