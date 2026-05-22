"""Job posting model."""

from __future__ import annotations

import enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import Index, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.models._mixins import TimestampMixin, UUIDPKMixin


class JobSource(str, enum.Enum):
    manual = "manual"
    url_paste = "url_paste"
    greenhouse = "greenhouse"
    lever = "lever"
    ashby = "ashby"
    workable = "workable"


class JobStatus(str, enum.Enum):
    discovered = "discovered"
    archived = "archived"
    expired = "expired"


class Job(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "job"

    source: Mapped[JobSource] = mapped_column(SAEnum(JobSource, name="jobsource"), nullable=False)
    source_id: Mapped[str | None] = mapped_column(String(200))
    url: Mapped[str | None] = mapped_column(String(2000))
    company: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    location: Mapped[str | None] = mapped_column(String(200))
    remote: Mapped[bool] = mapped_column(default=False, nullable=False)
    description_md: Mapped[str] = mapped_column(Text, nullable=False)
    raw_html: Mapped[str | None] = mapped_column(Text)
    salary_min_lpa: Mapped[float | None] = mapped_column()
    salary_max_lpa: Mapped[float | None] = mapped_column()
    seniority: Mapped[str | None] = mapped_column(String(60))
    visa_required: Mapped[bool | None] = mapped_column()
    extracted: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
    status: Mapped[JobStatus] = mapped_column(
        SAEnum(JobStatus, name="jobstatus"),
        nullable=False,
        default=JobStatus.discovered,
    )
    match_score: Mapped[int | None] = mapped_column(Integer)

    __table_args__ = (
        UniqueConstraint("source", "source_id", name="uq_job_source_sourceid"),
        Index("ix_job_company_title", "company", "title"),
    )
