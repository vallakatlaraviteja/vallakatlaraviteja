# hireloop — architecture

## Goal

Maximize the owner's probability of signing a full-time IT/software offer at ≥ ₹4.5 LPA fixed by 15 Jul 2026 — and serve as a portfolio piece recruiters can read in five minutes and believe.

## Non-goals (V0)

- Multi-tenant SaaS, billing, orgs, roles
- Auto-apply, scraping, mass outreach (see ADR 0003)
- AI mock interviewer, video coaching, "career strategist" chat
- Mobile / browser-extension surfaces

## Components

```
┌─────────────────────────┐    ┌──────────────────────────────┐
│  Web (Next.js 14)       │    │  Worker (RQ)                 │
│  - Cockpit              │    │  - Tailoring jobs            │
│  - Jobs / Applications  │    │  - JD enrichment             │
│  - Tailoring view       │    │  - Embedding indexing        │
│  - Daily cadence        │    │  - PDF rendering             │
└──────────┬──────────────┘    └─────────────┬────────────────┘
           │ REST + cookie session            │
┌──────────▼──────────────────────────────────▼────────────────┐
│  API (FastAPI)                                                │
│  /healthz /readyz                                             │
│  /api/auth   /api/candidate   /api/jobs   /api/applications   │
│  /api/tailoring   /api/cadence   /api/events   /api/analytics │
└──────────┬───────────────────────────────────────────────────┘
           │
┌──────────▼─────────────┐    ┌─────────────────────────────┐
│  Postgres + pgvector   │    │  Redis                      │
│  candidate, job,       │    │  rq queues, rate-limit,     │
│  application, event,   │    │  cache                      │
│  tailoring_run,        │    │                             │
│  embedding (V2)        │    │                             │
└────────────────────────┘    └─────────────────────────────┘
```

## Data model (V0)

- **candidate** — exactly one row in single-owner mode. Stores base resume (Markdown), constraints (target titles, geo, comp, sponsorship), and free-form profile facts.
- **job** — a job posting. Created via URL paste (we fetch + parse) or manual paste. Sources: `manual`, `url_paste`, `greenhouse`, `lever`, `ashby`, `workable`.
- **application** — pipeline state for one (candidate, job) pair. Linear status enum: saved → tailoring → ready_to_apply → applied → recruiter_screen → tech_screen → onsite → offer → accepted, plus rejected / withdrawn.
- **tailoring_run** — async LLM job: takes (resume, JD) → produces tailored resume Markdown + diff. Tracks tokens + cost.
- **event** — append-only audit log. Powers the timeline UI and analytics.

## Phases of delivery

1. **1A — Foundation (this commit):** Docker stack runs; healthz/readyz green; auth login works; jobs CRUD works; first migration applied; events recorded.
2. **1B — Pipeline core:** Applications CRUD + status transitions + funnel analytics endpoint.
3. **1C — Web cockpit:** Pipeline kanban view, application detail, event timeline.
4. **2 — AI Tailoring:** AIProvider adapter (Claude + OpenAI embeddings); RQ task; tailoring view.
5. **3 — Daily cadence:** Checklist model + streak + reminders.
6. **4 — Polish + deploy:** Fly.io; CI green; first real use against real JDs.

## Security

- Owner-only cookie session (httponly, samesite=lax, secure in non-local).
- All secrets via env. No keys in repo.
- DB connections pool with `pool_pre_ping`.
- Outbound fetcher times out at 15s, follows redirects, identifies its UA.
- LLM calls go through the adapter — easy to add per-call cost ceilings, redaction of PII, prompt-injection defense (V1).

## Observability

- structlog JSON logs in non-local environments.
- Sentry for unhandled exceptions (DSN optional).
- OpenTelemetry-ready (instrumentation libs available; not enabled in V0 to keep startup time low).
- Per-tailoring cost + token counts persisted on `tailoring_run`.
