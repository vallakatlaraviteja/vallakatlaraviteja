# Raviteja Vallakatla

**Backend & DevOps Engineer · Python · Docker · Document Intelligence**

Hyderabad, India · +91 75699 15450 · ravitejavallakatla@gmail.com
[LinkedIn](https://linkedin.com/in/raviteja-vallakatla9848/) · [GitHub](https://github.com/vallakatlaraviteja)

---

## Summary

Backend engineer with ~1 year of production experience shipping a multi-service OCR / document-intelligence platform. Owns end-to-end deployment across UAT, PreProd, and Production on Linux + Docker. Comfortable with multi-database migrations across Oracle, MySQL, and MS SQL Server, and ABBYY OCR service operations. Looking for an SDE-1 backend role at a product team in Hyderabad or remote-from-India.

---

## Experience

### Algonox Technologies Pvt Ltd — *Software Engineer (Trainee Program)*
*Hyderabad, India · Jun 2025 – Present*

- Built a document-aware **PDF rotation and skew-correction module** for the OCR pipeline using a 4-method scoring system (OCR confidence, projection variance, structural-line detection, aspect ratio) with weighted combination per document type — improved extraction accuracy on tilted/rotated scans by **~XX%** *(insert your real number; if unknown, omit "by ~XX%" — never fabricate).*
- Owned **end-to-end deployment** of the OCR document-classification system across UAT, PreProd, and Production environments, including Docker image builds, `docker-compose` orchestration, and zero-downtime container recreation for `camundaworkflow`, `business_rules_api`, and `prediction_api` services.
- Executed **schema and data migrations** across Oracle SQL, MySQL, and MS SQL Server — DDL scripts, data inserts, pre-migration backups, and post-deployment sanity checks — supporting client-environment rollouts.
- Managed **ABBYY OCR systemd service** configuration, environment variables, and license activation across multiple client deployments on Linux servers.
- Performed structured **code reviews** on backend Python modules; enforced exception-handling, logging, and query-optimization standards on Oracle and MySQL.
- Supported **UAT release validation** and post-deployment stability checks; reduced post-release defects by tightening sanity-check coverage before go-live.

---

## Projects

### `doc-skew-detector` — Document skew detection & correction
*Python, OpenCV, pytesseract, PyMuPDF, Docker · [github.com/vallakatlaraviteja/doc-skew-detector](https://github.com/vallakatlaraviteja/doc-skew-detector)*

- Open-source CLI library that detects skew/rotation in scanned PDFs and images using **four detection methods** (projection profile, Hough transform, Tesseract OSD, FFT) combined with weighted scoring and confidence-thresholding.
- Reaches **>X% correction accuracy** *(fill from your test set)* on the FUNSD scanned-form benchmark; runs in **<Y ms/page** on a single CPU core.
- Packaged as a Dockerized CLI; CI runs lint + pytest on every push.

### `multi-db-migrate` — Multi-database migration tool
*Python, SQLAlchemy, Alembic, Docker Compose · [github.com/vallakatlaraviteja/multi-db-migrate](https://github.com/vallakatlaraviteja/multi-db-migrate)*

- Idempotent schema and data migrations across **Oracle XE, MySQL, and MS SQL Server** with `up`, `down`, `status`, `dry-run`, and pre-migration backup commands.
- Single `docker-compose.yml` boots all three databases for local testing; covers DDL, DML, and rollback scenarios.

### `pyservice-template` — Production-grade FastAPI service template
*FastAPI, Pydantic v2, SQLAlchemy async, Postgres, Redis, Docker · [github.com/vallakatlaraviteja/pyservice-template](https://github.com/vallakatlaraviteja/pyservice-template)*

- Reference template for a backend service with structured logging, request-ID middleware, async Postgres + Redis, OpenTelemetry tracing, multi-stage non-root Docker image, and GitHub Actions CI.
- Covers `/healthz`, `/readyz`, and an example CRUD resource with full pytest coverage.

---

## Technical Skills

- **Backend:** Python, FastAPI, REST APIs, microservices, production debugging
- **Databases:** Oracle SQL, MySQL, MS SQL Server, schema design, query optimization
- **DevOps & Infra:** Docker, docker-compose, Linux server administration, CI/CD, AWS (basic)
- **Tools:** Git, Oracle SQL Developer, pytest, GitHub Actions
- **Languages (other):** C++, JavaScript (basic)
- **Domain:** OCR / document intelligence (ABBYY, Tesseract)

---

## Education

**B.Tech, Computer Science** — Jayamukhi Institute of Technological Sciences, Warangal · 2021 – 2025
CGPA: 8.01 / 10
