"""Tailoring runs — async job that generates a tailored resume from a JD + base resume."""

from __future__ import annotations

import enum
import uuid

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.models._mixins import TimestampMixin, UUIDPKMixin


class TailoringStatus(str, enum.Enum):
    queued = "queued"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"


class TailoringRun(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "tailoring_run"

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
    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("job.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    status: Mapped[TailoringStatus] = mapped_column(
        SAEnum(TailoringStatus, name="tailoringstatus"),
        default=TailoringStatus.queued,
        nullable=False,
    )
    rq_job_id: Mapped[str | None] = mapped_column(Text)
    input_resume_md: Mapped[str] = mapped_column(Text, nullable=False)
    output_resume_md: Mapped[str | None] = mapped_column(Text)
    diff_md: Mapped[str | None] = mapped_column(Text)
    cost_usd_micro: Mapped[int | None] = mapped_column(Integer)
    tokens_in: Mapped[int | None] = mapped_column(Integer)
    tokens_out: Mapped[int | None] = mapped_column(Integer)
    error: Mapped[str | None] = mapped_column(Text)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, default=dict, nullable=False)
