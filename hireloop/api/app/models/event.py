"""Event model — append-only log of pipeline state changes and notable actions."""

from __future__ import annotations

import enum
import uuid

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.models._mixins import TimestampMixin, UUIDPKMixin


class EventKind(str, enum.Enum):
    application_status_changed = "application_status_changed"
    application_created = "application_created"
    job_imported = "job_imported"
    tailoring_started = "tailoring_started"
    tailoring_completed = "tailoring_completed"
    tailoring_failed = "tailoring_failed"
    cadence_completed = "cadence_completed"
    note_added = "note_added"
    outreach_sent = "outreach_sent"


class Event(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "event"

    candidate_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("candidate.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    application_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("application.id", ondelete="CASCADE"),
        index=True,
    )
    job_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("job.id", ondelete="CASCADE"),
        index=True,
    )
    kind: Mapped[EventKind] = mapped_column(SAEnum(EventKind, name="eventkind"), nullable=False, index=True)
    summary: Mapped[str] = mapped_column(String(500), nullable=False)
    payload: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
