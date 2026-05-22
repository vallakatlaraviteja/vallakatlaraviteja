"""Job routes — list, create from URL or pasted text, get one, archive."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import require_owner
from app.db import get_session
from app.models.event import EventKind
from app.models.job import Job, JobSource, JobStatus
from app.schemas.job import JobCreate, JobOut
from app.services.candidate_service import get_or_create_owner
from app.services.event_service import record_event
from app.services.job_ingest import fetch_jd

router = APIRouter()


@router.get("", response_model=list[JobOut], summary="List jobs")
async def list_jobs(
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
    status_: JobStatus | None = Query(None, alias="status"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
) -> list[JobOut]:
    stmt = select(Job).order_by(Job.created_at.desc()).limit(limit).offset(offset)
    if status_:
        stmt = stmt.where(Job.status == status_)
    rows = (await session.execute(stmt)).scalars().all()
    return [JobOut.model_validate(r) for r in rows]


@router.post("", response_model=JobOut, status_code=status.HTTP_201_CREATED, summary="Create a job from URL or pasted text")
async def create_job(
    payload: JobCreate,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> JobOut:
    if not payload.url and not (payload.description_md and payload.company and payload.title):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide either `url` or all of (`company`, `title`, `description_md`).",
        )

    description = payload.description_md or ""
    company = payload.company or ""
    title = payload.title or ""
    raw_html: str | None = None
    src = JobSource.manual

    if payload.url:
        src = JobSource.url_paste
        fetched = await fetch_jd(str(payload.url))
        description = description or fetched["description_md"]
        title = title or fetched["title"]
        company = company or fetched["company_hint"] or "Unknown"
        raw_html = fetched["raw_html"]

    if not description.strip():
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Empty job description")

    job = Job(
        source=src,
        url=str(payload.url) if payload.url else None,
        company=company,
        title=title,
        location=payload.location,
        remote=payload.remote,
        description_md=description,
        raw_html=raw_html,
        salary_min_lpa=payload.salary_min_lpa,
        salary_max_lpa=payload.salary_max_lpa,
        seniority=payload.seniority,
    )
    session.add(job)
    await session.flush()

    owner = await get_or_create_owner(session)
    await record_event(
        session,
        candidate_id=owner.id,
        kind=EventKind.job_imported,
        summary=f"Imported {job.company} — {job.title}",
        job_id=job.id,
        payload={"source": src.value, "url": job.url},
    )
    await session.commit()
    await session.refresh(job)
    return JobOut.model_validate(job)


@router.get("/{job_id}", response_model=JobOut, summary="Get one job")
async def get_job(
    job_id: uuid.UUID,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> JobOut:
    job = await session.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return JobOut.model_validate(job)


@router.post("/{job_id}/archive", response_model=JobOut, summary="Archive a job")
async def archive_job(
    job_id: uuid.UUID,
    _: str = Depends(require_owner),
    session: AsyncSession = Depends(get_session),
) -> JobOut:
    job = await session.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    job.status = JobStatus.archived
    await session.commit()
    await session.refresh(job)
    return JobOut.model_validate(job)
