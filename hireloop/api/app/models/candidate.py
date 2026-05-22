"""Candidate model — the owner of this hireloop instance.

In single-user mode there is exactly one row in this table. The same shape
extends cleanly to multi-tenant.
"""

from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.models._mixins import TimestampMixin, UUIDPKMixin


class Candidate(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "candidate"

    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    location: Mapped[str | None] = mapped_column(String(200))
    headline: Mapped[str | None] = mapped_column(String(300))
    summary: Mapped[str | None] = mapped_column(Text)

    # Resume — stored as Markdown for diff-friendliness; PDF is rendered on demand.
    base_resume_md: Mapped[str | None] = mapped_column(Text)

    # Job-search constraints used by the matcher and gate filters.
    # Example:
    #   {
    #     "target_titles": ["Software Engineer", "Backend Engineer", "SDE-1"],
    #     "geo": ["Hyderabad", "Bangalore", "Remote-IN"],
    #     "needs_sponsorship": false,
    #     "min_comp_lpa": 4.5,
    #     "blocklist_companies": ["Algonox"]
    #   }
    constraints: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)

    # Free-form profile facts the AI uses for tailoring (skills, projects, achievements).
    profile: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
