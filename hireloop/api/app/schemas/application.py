"""Application request/response shapes."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.application import ApplicationStatus
from app.schemas.job import JobOut


class ApplicationCreate(BaseModel):
    job_id: uuid.UUID
    notes_md: str | None = None
    referrer_name: str | None = Field(None, max_length=200)
    referrer_email: EmailStr | None = None


class ApplicationUpdate(BaseModel):
    status: ApplicationStatus | None = None
    next_action: str | None = Field(None, max_length=300)
    next_action_due: datetime | None = None
    notes_md: str | None = None
    referrer_name: str | None = Field(None, max_length=200)
    referrer_email: EmailStr | None = None
    applied_at: datetime | None = None


class ApplicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    candidate_id: uuid.UUID
    job_id: uuid.UUID
    status: ApplicationStatus
    applied_at: datetime | None
    next_action: str | None
    next_action_due: datetime | None
    referrer_name: str | None
    referrer_email: EmailStr | None
    notes_md: str | None
    metadata_: dict[str, Any] = Field(alias="metadata_")
    created_at: datetime
    updated_at: datetime
    job: JobOut
