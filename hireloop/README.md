# hireloop

Personal AI job-acquisition cockpit. Built by [@vallakatlaraviteja](https://github.com/vallakatlaraviteja) to escape an exploitative trainee role and land a real SDE-1 backend offer in 6 weeks.

> Ships features only when they directly improve the owner's hiring probability. No feature theater.

## What it is

Three things, scoped tight:

1. **Application CRM** — pipeline tracker across `discovered → tailored → applied → recruiter screen → tech screen → onsite → offer / rejected`, with follow-up reminders and funnel analytics.
2. **AI Resume Tailoring** — paste a job-description URL or text → service fetches, parses, generates tailored bullet diffs against the base resume via Claude → review/edit → export PDF.
3. **Daily Cadence Enforcer** — daily checklist (LeetCode, applications, outreach), streak tracking, and reminder cadence.

## What it deliberately is not

No auto-apply. No LinkedIn / Indeed / Naukri scraping. No mass cold outreach. No mock-interview AI. No multi-tenant SaaS. No billing. See `docs/adr/0003-no-scraping-no-autoapply.md`.

## Stack

FastAPI · Postgres 16 + pgvector · Redis 7 + RQ · Next.js 14 (App Router, TypeScript, Tailwind, shadcn/ui) · Anthropic Claude · OpenAI embeddings · Docker Compose · Fly.io.

## Run locally

```bash
cp .env.example .env          # fill in ANTHROPIC_API_KEY, OPENAI_API_KEY, OWNER_EMAIL
docker compose up --build
# api:    http://localhost:8000  (OpenAPI: /docs)
# web:    http://localhost:3000
# worker: logs only
```

Run database migrations:

```bash
docker compose exec api alembic upgrade head
docker compose exec api python -m ops.seed
```

## Layout

```
hireloop/
├── api/               FastAPI backend + Alembic migrations + tests
├── web/               Next.js 14 cockpit
├── worker/            RQ worker entrypoint
├── ops/               seed scripts, deploy helpers
├── docs/              architecture + ADRs
└── docker-compose.yml
```

## Status

Phase 1A — foundation. See `docs/architecture.md` for the full plan.

## License

MIT.
