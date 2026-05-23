"""FastAPI application entrypoint."""

from __future__ import annotations

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import get_settings
from app.core.logging import configure_logging, get_logger
from app.routers import analytics, applications, auth, candidate, events, health, jobs

configure_logging()
log = get_logger(__name__)
settings = get_settings()

if settings.sentry_dsn:
    sentry_sdk.init(dsn=settings.sentry_dsn, environment=settings.environment, traces_sample_rate=0.1)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hireloop API",
        version=__version__,
        description="Personal AI job-acquisition cockpit. Single-user mode.",
        docs_url="/docs",
        redoc_url=None,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)
    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    app.include_router(candidate.router, prefix="/api/candidate", tags=["candidate"])
    app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])
    app.include_router(applications.router, prefix="/api/applications", tags=["applications"])
    app.include_router(events.router, prefix="/api/events", tags=["events"])
    app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

    @app.on_event("startup")
    async def _startup() -> None:
        log.info("api.startup", environment=settings.environment, owner=settings.owner_email)

    return app


app = create_app()
