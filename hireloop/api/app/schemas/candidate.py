"""Candidate request/response shapes."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CandidateBase(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=200)
    location: str | None = None
    headline: str | None = None
    summary: str | None = None
    base_resume_md: str | None = None
    constraints: dict[str, Any] = Field(default_factory=dict)
    profile: dict[str, Any] = Field(default_factory=dict)


class CandidateUpdate(CandidateBase):
    full_name: str | None = None  # type: ignore[assignment]


class CandidateOut(CandidateBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
    created_at: datetime
    updated_at: datetime
