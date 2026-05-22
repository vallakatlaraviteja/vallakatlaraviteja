"""Candidate (owner) profile routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import require_owner
from app.db import get_session
from app.schemas.candidate import CandidateOut, CandidateUpdate
from app.services.candidate_service import get_or_create_owner, update_owner

router = APIRouter()


@router.get("", response_model=CandidateOut, summary="Get the owner profile")
async def get_me(
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> CandidateOut:
    row = await get_or_create_owner(session)
    await session.commit()
    return CandidateOut.model_validate(row)


@router.put("", response_model=CandidateOut, summary="Update the owner profile")
async def put_me(
    payload: CandidateUpdate,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> CandidateOut:
    row = await update_owner(session, payload)
    await session.commit()
    return CandidateOut.model_validate(row)
