"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-05-22

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


APP_STATUS = (
    "saved",
    "tailoring",
    "ready_to_apply",
    "applied",
    "recruiter_screen",
    "tech_screen",
    "onsite",
    "offer",
    "accepted",
    "rejected",
    "withdrawn",
)
JOB_SOURCE = ("manual", "url_paste", "greenhouse", "lever", "ashby", "workable")
JOB_STATUS = ("discovered", "archived", "expired")
TAILORING_STATUS = ("queued", "running", "succeeded", "failed")
EVENT_KIND = (
    "application_status_changed",
    "application_created",
    "job_imported",
    "tailoring_started",
    "tailoring_completed",
    "tailoring_failed",
    "cadence_completed",
    "note_added",
    "outreach_sent",
)


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "candidate",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("email", sa.String(320), nullable=False, unique=True),
        sa.Column("full_name", sa.String(200), nullable=False),
        sa.Column("location", sa.String(200)),
        sa.Column("headline", sa.String(300)),
        sa.Column("summary", sa.Text()),
        sa.Column("base_resume_md", sa.Text()),
        sa.Column("constraints", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default="{}"),
        sa.Column("profile", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default="{}"),
    )
    op.create_index("ix_candidate_email", "candidate", ["email"], unique=True)

    op.execute(f"CREATE TYPE jobsource AS ENUM ({', '.join(repr(v) for v in JOB_SOURCE)})")
    op.execute(f"CREATE TYPE jobstatus AS ENUM ({', '.join(repr(v) for v in JOB_STATUS)})")

    op.create_table(
        "job",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("source", postgresql.ENUM(*JOB_SOURCE, name="jobsource", create_type=False), nullable=False),
        sa.Column("source_id", sa.String(200)),
        sa.Column("url", sa.String(2000)),
        sa.Column("company", sa.String(200), nullable=False),
        sa.Column("title", sa.String(300), nullable=False),
        sa.Column("location", sa.String(200)),
        sa.Column("remote", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("description_md", sa.Text(), nullable=False),
        sa.Column("raw_html", sa.Text()),
        sa.Column("salary_min_lpa", sa.Float()),
        sa.Column("salary_max_lpa", sa.Float()),
        sa.Column("seniority", sa.String(60)),
        sa.Column("visa_required", sa.Boolean()),
        sa.Column("extracted", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default="{}"),
        sa.Column("status", postgresql.ENUM(*JOB_STATUS, name="jobstatus", create_type=False), nullable=False, server_default="discovered"),
        sa.Column("match_score", sa.Integer()),
        sa.UniqueConstraint("source", "source_id", name="uq_job_source_sourceid"),
    )
    op.create_index("ix_job_company", "job", ["company"])
    op.create_index("ix_job_company_title", "job", ["company", "title"])

    op.execute(f"CREATE TYPE applicationstatus AS ENUM ({', '.join(repr(v) for v in APP_STATUS)})")

    op.create_table(
        "application",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("candidate_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("candidate.id", ondelete="CASCADE"), nullable=False),
        sa.Column("job_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("job.id", ondelete="CASCADE"), nullable=False),
        sa.Column("status", postgresql.ENUM(*APP_STATUS, name="applicationstatus", create_type=False), nullable=False, server_default="saved"),
        sa.Column("applied_at", sa.DateTime(timezone=True)),
        sa.Column("next_action", sa.String(300)),
        sa.Column("next_action_due", sa.DateTime(timezone=True)),
        sa.Column("referrer_name", sa.String(200)),
        sa.Column("referrer_email", sa.String(320)),
        sa.Column("notes_md", sa.Text()),
        sa.Column("tailored_resume_md", sa.Text()),
        sa.Column("tailored_resume_pdf_path", sa.String(500)),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default="{}"),
    )
    op.create_index("ix_application_candidate_id", "application", ["candidate_id"])
    op.create_index("ix_application_job_id", "application", ["job_id"])
    op.create_index("ix_application_status", "application", ["status"])
    op.create_index("ix_application_next_action_due", "application", ["next_action_due"])

    op.execute(f"CREATE TYPE tailoringstatus AS ENUM ({', '.join(repr(v) for v in TAILORING_STATUS)})")

    op.create_table(
        "tailoring_run",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("candidate_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("candidate.id", ondelete="CASCADE"), nullable=False),
        sa.Column("application_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("application.id", ondelete="CASCADE")),
        sa.Column("job_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("job.id", ondelete="CASCADE"), nullable=False),
        sa.Column("status", postgresql.ENUM(*TAILORING_STATUS, name="tailoringstatus", create_type=False), nullable=False, server_default="queued"),
        sa.Column("rq_job_id", sa.Text()),
        sa.Column("input_resume_md", sa.Text(), nullable=False),
        sa.Column("output_resume_md", sa.Text()),
        sa.Column("diff_md", sa.Text()),
        sa.Column("cost_usd_micro", sa.Integer()),
        sa.Column("tokens_in", sa.Integer()),
        sa.Column("tokens_out", sa.Integer()),
        sa.Column("error", sa.Text()),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default="{}"),
    )
    op.create_index("ix_tailoring_run_candidate_id", "tailoring_run", ["candidate_id"])
    op.create_index("ix_tailoring_run_application_id", "tailoring_run", ["application_id"])
    op.create_index("ix_tailoring_run_job_id", "tailoring_run", ["job_id"])

    op.execute(f"CREATE TYPE eventkind AS ENUM ({', '.join(repr(v) for v in EVENT_KIND)})")

    op.create_table(
        "event",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("candidate_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("candidate.id", ondelete="CASCADE"), nullable=False),
        sa.Column("application_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("application.id", ondelete="CASCADE")),
        sa.Column("job_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("job.id", ondelete="CASCADE")),
        sa.Column("kind", postgresql.ENUM(*EVENT_KIND, name="eventkind", create_type=False), nullable=False),
        sa.Column("summary", sa.String(500), nullable=False),
        sa.Column("payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default="{}"),
    )
    op.create_index("ix_event_candidate_id", "event", ["candidate_id"])
    op.create_index("ix_event_application_id", "event", ["application_id"])
    op.create_index("ix_event_job_id", "event", ["job_id"])
    op.create_index("ix_event_kind", "event", ["kind"])


def downgrade() -> None:
    op.drop_table("event")
    op.execute("DROP TYPE eventkind")
    op.drop_table("tailoring_run")
    op.execute("DROP TYPE tailoringstatus")
    op.drop_table("application")
    op.execute("DROP TYPE applicationstatus")
    op.drop_table("job")
    op.execute("DROP TYPE jobstatus")
    op.execute("DROP TYPE jobsource")
    op.drop_table("candidate")
