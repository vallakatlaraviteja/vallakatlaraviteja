"""RQ worker entrypoint.

Picks up jobs from the `default` queue. In Phase 2 we add tailoring tasks here.
"""

from __future__ import annotations

from redis import Redis
from rq import Queue, Worker

from app.config import get_settings
from app.core.logging import configure_logging, get_logger

configure_logging()
log = get_logger(__name__)


def main() -> None:
    settings = get_settings()
    log.info("worker.boot", redis=settings.redis_url, environment=settings.environment)
    conn = Redis.from_url(settings.redis_url)
    queues = [Queue("default", connection=conn), Queue("tailoring", connection=conn)]
    worker = Worker(queues, connection=conn)
    worker.work(with_scheduler=True)


if __name__ == "__main__":
    main()
