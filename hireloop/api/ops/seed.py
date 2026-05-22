"""Seed the owner profile from .env values + a base resume.

Runs once after `alembic upgrade head`. Idempotent.
"""

from __future__ import annotations

import asyncio

from app.config import get_settings
from app.core.logging import configure_logging, get_logger
from app.db import AsyncSessionLocal
from app.services.candidate_service import get_or_create_owner

configure_logging()
log = get_logger(__name__)

DEFAULT_CONSTRAINTS = {
    "target_titles": [
        "Software Engineer",
        "Backend Engineer",
        "SDE-1",
        "Junior Software Engineer",
        "Python Developer",
    ],
    "geo": ["Hyderabad", "Bangalore", "Pune", "Chennai", "Remote-IN"],
    "needs_sponsorship": False,
    "min_comp_lpa": 4.5,
    "blocklist_companies": [],
}

DEFAULT_PROFILE = {
    "skills": {
        "primary": ["Python", "FastAPI", "Docker", "Linux", "PostgreSQL", "MySQL", "Oracle SQL"],
        "secondary": ["C++", "JavaScript", "AWS"],
        "domain": ["OCR", "Document Intelligence", "ABBYY"],
    },
    "current_role": {
        "company": "Algonox Technologies",
        "title": "Software Engineer (Trainee Program)",
        "start": "2025-06-01",
        "end": None,
    },
    "education": {
        "degree": "B.Tech, Computer Science",
        "institution": "Jayamukhi Institute of Technological Sciences, Warangal",
        "start": 2021,
        "end": 2025,
        "cgpa": 8.01,
    },
}


async def main() -> None:
    settings = get_settings()
    async with AsyncSessionLocal() as session:
        owner = await get_or_create_owner(session)
        if not owner.constraints:
            owner.constraints = DEFAULT_CONSTRAINTS
        if not owner.profile:
            owner.profile = DEFAULT_PROFILE
        if not owner.location:
            owner.location = "Hyderabad, India"
        if not owner.headline:
            owner.headline = "Backend & DevOps Engineer · Python · Docker · Document Intelligence"
        await session.commit()
        log.info("seed.ok", email=settings.owner_email)


if __name__ == "__main__":
    asyncio.run(main())
