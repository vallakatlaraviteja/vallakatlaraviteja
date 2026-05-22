# ADR 0003 — No scraping, no auto-apply, no mass outreach

**Status:** Accepted · 2026-05-22

## Context

Many "AI job platforms" market themselves on automation: scraping LinkedIn / Indeed / Naukri, auto-applying to jobs, mass-DMing recruiters. Several of those products either (a) get sued/banned or (b) measurably hurt their users' interview-conversion rates.

The owner of this instance needs a real offer in 6 weeks. Burning their professional brand or getting flagged by ATS is not an acceptable failure mode.

## Decision

**hireloop will never:**

1. **Scrape job boards.** No LinkedIn, Indeed, Naukri, Glassdoor scraping. Their ToS forbid it; many enforce via IP/account bans and CFAA-equivalent legal action. (`hiQ v. LinkedIn` did NOT make scraping safe.)
2. **Auto-apply to jobs.** Several ATS (Workday, Greenhouse, Lever) detect bots and flag candidates. Recruiters share blacklists. It also requires the candidate to "certify this is my own work" — which auto-apply violates.
3. **Mass-send cold outreach.** CAN-SPAM / GDPR / Indian IT Act compliance is non-trivial; templated mass-outreach has measurably worse reply rates than 5 manual messages a day.

## What we DO

1. **JD ingest from owner-provided URLs.** Owner pastes a URL → we make ONE polite GET with a clear User-Agent identifying ourselves, parse with Readability, store. No crawling, no following links. ToS-clean for personal use.
2. **JD ingest from pasted text.** Owner copies a JD into the cockpit; we store it. No fetching at all.
3. **Legitimate ATS public boards (V1).** Greenhouse, Lever, Ashby, Workable expose public board APIs — we use them within their published rate limits.
4. **Outreach drafting (V1, maybe).** We draft a personalized first message per target; the owner reviews and sends from their own LinkedIn/email manually. No automation.

## Consequences

- **Positive:** zero ToS exposure, owner's brand stays clean, we do not reproduce the failure modes of LazyApply / Sonara / LoopCV.
- **Negative:** lower top-of-funnel volume than scraping bots produce. Acceptable: per ADR 0001 we believe positioning + tailoring + cadence > volume for this owner's funnel.
