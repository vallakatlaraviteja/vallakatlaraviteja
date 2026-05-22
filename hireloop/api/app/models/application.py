"""Application model — pipeline state for one job."""

from __future__ import annotations

import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base
from app.models._mixins import TimestampMixin, UUIDPKMixin


class ApplicationStatus(str, enum.Enum):
    """Linear pipeline. Branching to rejected/withdrawn from any stage."""

    saved = "saved"
    tailoring = "tailoring"
    ready_to_apply = "ready_to_apply"
    applied = "applied"
    recruiter_screen = "recruiter_screen"
    tech_screen = "tech_screen"
    onsite = "onsite"
    offer = "offer"
    accepted = "accepted"
    rejected = "rejected"
    withdrawn = "withdrawn"


class Application(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "application"

    candidate_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("candidate.id", ondelete="CASCADE"), nullable=False, index=True
    )
    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("job.id", ondelete="CASCADE"), nullable=False, index=True
    )

    status: Mapped[ApplicationStatus] = mapped_column(
        SAEnum(ApplicationStatus, name="applicationstatus"),
        default=ApplicationStatus.saved,
        nullable=False,
        index=True,
    )

    applied_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    next_action: Mapped[str | None] = mapped_column(String(300))
    next_action_due: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), index=True)

    referrer_name: Mapped[str | None] = mapped_column(String(200))
    referrer_email: Mapped[str | None] = mapped_column(String(320))

    notes_md: Mapped[str | None] = mapped_column(Text)

    # Tailored resume rendered for THIS application (Markdown source).
    tailored_resume_md: Mapped[str | None] = mapped_column(Text)
    tailored_resume_pdf_path: Mapped[str | None] = mapped_column(String(500))

    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict, nullable=False)

    job = relationship("Job", lazy="joined")
