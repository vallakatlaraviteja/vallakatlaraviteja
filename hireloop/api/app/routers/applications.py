"""Application routes — pipeline state for the owner's job hunt."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import require_owner
from app.db import get_session
from app.models.application import Application, ApplicationStatus
from app.schemas.application import ApplicationCreate, ApplicationOut, ApplicationUpdate
from app.services import application_service as svc
from app.services.candidate_service import get_or_create_owner

router = APIRouter()


@router.get("", response_model=list[ApplicationOut], summary="List applications")
async def list_applications(
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
    status_: ApplicationStatus | None = Query(None, alias="status"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
) -> list[ApplicationOut]:
    owner = await get_or_create_owner(session)
    rows = await svc.list_applications(
        session, candidate_id=owner.id, status=status_, limit=limit, offset=offset
    )
    await session.commit()
    return [ApplicationOut.model_validate(r) for r in rows]



@router.post(
    "",
    response_model=ApplicationOut,
    status_code=status.HTTP_201_CREATED,
    summary="Save a job into the pipeline",
)
async def create_application(
    payload: ApplicationCreate,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> ApplicationOut:
    owner = await get_or_create_owner(session)
    try:
        row = await svc.create_application(
            session,
            candidate_id=owner.id,
            job_id=payload.job_id,
            notes_md=payload.notes_md,
            referrer_name=payload.referrer_name,
            referrer_email=str(payload.referrer_email) if payload.referrer_email else None,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    await session.commit()
    await session.refresh(row, attribute_names=["job"])
    return ApplicationOut.model_validate(row)


@router.get("/{application_id}", response_model=ApplicationOut, summary="Get one application")
async def get_application(
    application_id: uuid.UUID,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> ApplicationOut:
    row = await session.get(Application, application_id)
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return ApplicationOut.model_validate(row)



@router.patch("/{application_id}", response_model=ApplicationOut, summary="Update an application")
async def update_application(
    application_id: uuid.UUID,
    payload: ApplicationUpdate,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> ApplicationOut:
    row = await session.get(Application, application_id)
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")

    data = payload.model_dump(exclude_unset=True)
    target_status = data.pop("status", None)
    if target_status is not None:
        try:
            await svc.transition_status(session, application=row, target=target_status)
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    for field, value in data.items():
        if field == "referrer_email" and value is not None:
            value = str(value)
        setattr(row, field, value)

    await session.commit()
    await session.refresh(row, attribute_names=["job"])
    return ApplicationOut.model_validate(row)
