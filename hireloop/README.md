# hireloop

Personal AI job-acquisition cockpit. Built by [@vallakatlaraviteja](https://github.com/vallakatlaraviteja) to run a focused, measurable job hunt.

> Ships features only when they directly improve the owner's hiring probability. No feature theater.

## What it is

Three features, scoped tight:

1. **Application CRM** — pipeline tracker across `saved → tailoring → ready_to_apply → applied → recruiter_screen → tech_screen → onsite → offer → accepted`, with `rejected` / `withdrawn` reachable from any active stage. Append-only event log, follow-up reminders, and funnel analytics.
2. **AI Resume Tailoring** *(roadmap — Phase 2)* — paste a job-description URL or text → service fetches, parses, generates tailored bullet diffs against the base resume via Claude → review/edit → export PDF.
3. **Daily Cadence Enforcer** *(roadmap — Phase 3)* — daily checklist (LeetCode, applications, outreach), streak tracking, and spaced repetition for revisit problems.

## What it deliberately is not

No auto-apply. No LinkedIn / Indeed / Naukri scraping. No mass cold outreach. No mock-interview AI. No multi-tenant SaaS. No billing. See [`docs/adr/0003-no-scraping-no-autoapply.md`](./docs/adr/0003-no-scraping-no-autoapply.md).

## Stack

FastAPI · SQLAlchemy 2.x async · Postgres 16 + pgvector · Redis 7 + RQ · Next.js 14 (App Router, TypeScript, Tailwind, TanStack Query) · Anthropic Claude *(Phase 2)* · OpenAI embeddings *(Phase 2)* · Docker Compose · Fly.io *(Phase 4)*.

## Run locally

```bash
cp .env.example .env          # fill in OWNER_EMAIL (and ANTHROPIC_API_KEY / OPENAI_API_KEY when Phase 2 lands)
docker compose up --build
# api:    http://localhost:8000  (OpenAPI: /docs)
# web:    http://localhost:3000
# worker: logs only
```

Run database migrations and seed:

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

**Phase 1B — pipeline core complete.** The application state machine, funnel analytics, kanban view, and JD-by-URL ingest are live. Phase 2 (AI tailoring), Phase 3 (daily cadence), and Phase 4 (Fly.io deploy) are queued — see [`docs/architecture.md`](./docs/architecture.md) for the full plan and [`docs/adr/`](./docs/adr) for locked decisions.

## License

MIT — see [`../LICENSE`](../LICENSE).
