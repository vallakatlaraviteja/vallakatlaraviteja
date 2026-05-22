# ADR 0001 — Stack lock-in

**Status:** Accepted · 2026-05-22

## Context

Single-owner V0. Owner is a Python/backend engineer. 6-week deadline to deliver three features (Application CRM, Resume Tailoring, Daily Cadence) that get *used daily*. Stack must be:

- learnable + debuggable by the owner
- shippable on free / very cheap infra
- credible to recruiters who open the repo

## Decision

| Layer | Choice | Why |
|---|---|---|
| API | FastAPI 0.115 + Pydantic v2 + SQLAlchemy 2.x async + Alembic | Owner's strongest language; best AI-library ecosystem; great OpenAPI; modern async. |
| DB | Postgres 16 + pgvector | Industry default; pgvector lets us colocate embeddings; free tier on every cloud. |
| Queue | Redis 7 + RQ | RQ is one-process simple; Celery is overkill for one user. Redis double-duties as cache + rate limit. |
| Worker | Python (RQ Worker) | Same image as API → one container, one deploy. |
| Web | Next.js 14 App Router + TS + Tailwind + shadcn/ui + TanStack Query | Modern, recruiter-recognizable, fast to ship; SSR not required (single-user) but App Router is the default. |
| LLM | Anthropic Claude (Sonnet) via `AIProvider` adapter | Best at writing tailored resume bullets without sounding AI-generated. |
| Embeddings | OpenAI `text-embedding-3-large` via the same adapter | Best price/quality for retrieval today; swappable. |
| Auth | Env-based single-owner cookie session (`itsdangerous`) | No multi-tenant complexity; swap to magic-link in V1 without touching call sites. |
| Deploy | Fly.io (or local Docker Compose) | Free tier sufficient for one user; fast deploys; not Vercel-locked. |
| Observability | structlog + Sentry + OpenTelemetry hooks | Production hygiene without paying for SaaS at this scale. |

## Consequences

- **Positive:** small surface area, zero-cost local dev, every component is something a recruiter at Tier-B Indian product cos has on their stack.
- **Negative:** Python + Node split means two language toolchains. Acceptable cost for the recruiter signal of having a polished frontend.
- **Reversible:** the `AIProvider` adapter, and the single-owner auth module, are explicitly designed to swap without app-wide changes.
