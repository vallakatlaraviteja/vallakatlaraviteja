# Raviteja Vallakatla

**Backend & DevOps Engineer · Python · Docker · Document Intelligence**

Hyderabad, India · [LinkedIn](https://linkedin.com/in/raviteja-vallakatla9848/) · ravitejavallakatla@gmail.com

Backend engineer with ~1 year of production experience shipping a multi-service OCR / document-intelligence platform. Owner of end-to-end deployments across UAT, PreProd, and Production on Linux + Docker. Comfortable with multi-database migrations across Oracle, MySQL, and MS SQL Server. Looking for an SDE-1 backend role at a product team in Hyderabad or remote-from-India.

---

## Featured projects

### [`hireloop`](./hireloop/) — Personal AI job-acquisition cockpit *(in active use)*

A production-grade FastAPI + Postgres + Next.js cockpit I built to run my own job hunt. Three features, scoped tight: application CRM with state-machine pipeline (`saved → applied → recruiter screen → tech → onsite → offer`), AI resume tailoring against pasted JDs, and a daily-cadence enforcer.

- **Stack:** FastAPI 0.115 · SQLAlchemy 2.x async · Postgres 16 + pgvector · Redis + RQ · Next.js 14 (App Router, TypeScript, Tailwind, TanStack Query) · Anthropic Claude · OpenAI embeddings · Docker Compose · GitHub Actions CI
- **Engineering choices captured as ADRs:** [stack lock-in](./hireloop/docs/adr/0001-stack.md) · [single-owner mode](./hireloop/docs/adr/0002-single-owner-mode.md) · [no-scraping / no-auto-apply policy](./hireloop/docs/adr/0003-no-scraping-no-autoapply.md)
- **Architecture:** [`hireloop/docs/architecture.md`](./hireloop/docs/architecture.md)
- **State machine:** pure-Python validator with full parametric test coverage of every legal/illegal pipeline transition ([`tests/test_state_machine.py`](./hireloop/api/tests/test_state_machine.py))
- **Funnel analytics:** `GET /api/analytics/funnel` derives stage counts and conversion rates from the append-only event log

### OCR Format Detection & Extraction Engine *(production work at Algonox)*

A document-aware OCR pipeline serving real client traffic across UAT / PreProd / Production environments.

- Designed a **PDF rotation & skew-correction module** with 4 scoring methods (OCR confidence, projection variance, structural-line detection, aspect ratio) combined with weighted per-document-type selection
- Owned **Docker / docker-compose deployments** for `camundaworkflow`, `business_rules_api`, and `prediction_api` services across multiple environments
- Executed **schema and data migrations** across Oracle SQL, MySQL, and MS SQL Server with DDL scripts, data inserts, pre-migration backups, and post-deployment sanity checks
- Managed **ABBYY OCR systemd service** configuration, env vars, and license activation across client deployments

---

## Experience

**Software Engineer (Trainee Program)** — Algonox Technologies Pvt. Ltd., Hyderabad · *Jun 2025 – Present*
Production OCR / document-intelligence platform. Backend Python, multi-DB migrations, Linux deployments, Docker microservices. See OCR project above for detail.

---

## Education

**B.Tech, Computer Science** — Jayamukhi Institute of Technological Sciences, Warangal · *2021 – 2025* · CGPA 8.01

---

## Skills

- **Backend:** Python, FastAPI, REST APIs, microservices, async SQLAlchemy
- **Databases:** Oracle SQL, MySQL, MS SQL Server, Postgres + pgvector
- **DevOps:** Docker, docker-compose, Linux, CI/CD, GitHub Actions, AWS basics
- **Tools:** Git, Alembic, pytest, structlog, OpenTelemetry-ready services
- **Domain:** OCR / document intelligence (ABBYY, Tesseract)

---

## How I work

Engineering decisions live as Architecture Decision Records, not folklore. Pull requests describe what changed and *why*, with stop-loss criteria for risky bets. See [`STRATEGY.md`](./STRATEGY.md) for the methodology I'm applying to my current job hunt — pressure-tested assumptions, target archetype, comp strategy, and a 6-week execution plan with measurable stop-loss triggers.
