"""SQLAlchemy ORM models. Importing this module registers all models with Base.metadata."""

from app.models.application import Application, ApplicationStatus
from app.models.candidate import Candidate
from app.models.event import Event, EventKind
from app.models.job import Job, JobSource, JobStatus
from app.models.tailoring import TailoringRun, TailoringStatus

__all__ = [
    "Application",
    "ApplicationStatus",
    "Candidate",
    "Event",
    "EventKind",
    "Job",
    "JobSource",
    "JobStatus",
    "TailoringRun",
    "TailoringStatus",
]
