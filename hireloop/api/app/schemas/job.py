"""Job request/response shapes."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from app.models.job import JobSource, JobStatus


class JobCreate(BaseModel):
    """Create a job either from a URL (we fetch+parse) or by pasting full text."""

    url: HttpUrl | None = None
    company: str | None = Field(None, max_length=200)
    title: str | None = Field(None, max_length=300)
    location: str | None = Field(None, max_length=200)
    remote: bool = False
    description_md: str | None = None
    salary_min_lpa: float | None = None
    salary_max_lpa: float | None = None
    seniority: str | None = None


class JobOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    source: JobSource
    source_id: str | None
    url: str | None
    company: str
    title: str
    location: str | None
    remote: bool
    description_md: str
    salary_min_lpa: float | None
    salary_max_lpa: float | None
    seniority: str | None
    visa_required: bool | None
    extracted: dict[str, Any]
    status: JobStatus
    match_score: int | None
    created_at: datetime
    updated_at: datetime
