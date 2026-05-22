"""Event response shape."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from app.models.event import EventKind


class EventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    candidate_id: uuid.UUID
    application_id: uuid.UUID | None
    job_id: uuid.UUID | None
    kind: EventKind
    summary: str
    payload: dict[str, Any]
    created_at: datetime
