# ADR 0002 — Single-owner mode

**Status:** Accepted · 2026-05-22

## Context

V0 is for one user — the repository owner — who is hunting for a job and will use this daily. Multi-tenant SaaS is out of scope until V1 (post-hire).

## Decision

The application runs in **single-owner mode**:

- `OWNER_EMAIL` is set in `.env`. Exactly one row in the `candidate` table corresponds to it.
- Auth is a cookie session signed with `SESSION_SECRET` via `itsdangerous`. Login = "is the email you're claiming the configured `OWNER_EMAIL`? if yes, issue session". No password, no email verification, no rate-limited brute-force protection (single user, low risk).
- All API endpoints depend on `require_owner`, which 401s without a session and 403s if the cookie is for a different email than `OWNER_EMAIL`.
- Schema is **already multi-tenant-shaped**: all owned rows reference `candidate_id`. Migrating to multi-tenant SaaS in V1 is a swap of the auth module + a candidate-row creation flow + per-tenant row-level filters. No table changes required.

## What we deliberately omit

- OAuth / Google / GitHub login
- Email verification / magic links
- Password reset, account recovery
- Org / team / role models
- Stripe / billing
- Per-user quotas, fair-use throttling

These are V1 concerns.

## Consequences

- **Positive:** ~1–2 weeks of auth/billing/SaaS infrastructure work avoided. Owner ships features that move the hiring metric.
- **Negative:** the V1 multi-tenant migration is non-trivial — but the schema is shaped to make it mechanical, not architectural.
