# Job Acquisition Strategy — Raviteja Vallakatla

**Status:** v1 — initial strategy
**Owner:** Raviteja Vallakatla
**Operating mode:** Critical Combat Mode (see `.kiro/steering/critical-combat-mode.md`)
**Primary metric:** Signed full-time offer at **≥ ₹4.5 LPA fixed**, Hyderabad / remote-from-India, **by 15 July 2026** (~6 weeks from 22 May 2026).

> This is not a job hunt. It is an escape from below-market exploitation labor.
> Every decision in this document is filtered through that lens.

---

## 1. Hard facts (no spin)

| Field | Value |
|---|---|
| Location | Hyderabad, India (origin: Warangal, Telangana) |
| Citizenship / passport | Indian citizen, **no passport** → India-only market |
| Education | B.Tech CS, Jayamukhi Inst. of Technological Sciences (tier-3 private), 2021–2025, CGPA 8.01 |
| Current employer | Algonox Technologies Pvt Ltd, Hyderabad |
| Current title | Software Engineer Trainee (Temporary) |
| Current pay | **₹10,000 / month** (~$120/mo) — below any legitimate market floor |
| Tenure at current | ~11 months (Jun 2025 – present) |
| FT conversion status | Not converted; situation is "they want my work" — no commitment |
| Bank balance | Hundreds of dollars only — financial emergency |
| Search runtime | ~6 months, inconsistent execution |
| Apps submitted | ~200 |
| Recruiter screens | ~25 (12% of apps — OK) |
| Tech screens | ~5 (20% of recruiter screens — **PRIMARY LEAK**) |
| Onsites | 1–2 |
| Offers | **0** |
| Public proof of skill | Empty — pretty README, no real repos |
| Hard deadline | Offer signed by 15 July 2026 |
| Comp floor (escape velocity) | ₹4.5 LPA fixed |


---

## 2. Diagnosis — why the funnel leaks

The funnel says **the leak is recruiter-screen → tech-screen**, not applications-to-screens. Top-of-funnel positioning is roughly OK; you're losing the candidate *after* the recruiter looks closely. Five typical causes — ranked by what's killing **you**, specifically:

1. **TITLE: "Software Engineer Trainee (Temporary)" with 11 months tenure.** Recruiters reading this think: *"Why hasn't his employer converted him? Either the company doesn't have headcount [signal: small/struggling], or he isn't good enough to convert [signal: avoid], or he tolerates poor terms [signal: he'll undersell himself, will jump again fast]."* Whichever interpretation, screen ends.

2. **NO PUBLIC PROOF.** The GitHub profile README is well-written narrative, but recruiters who click through find no repos with real code. Narrative without artifact is **worse than empty profile** — it sets expectation, then breaks it. Tier-3 college + Trainee title means GitHub is the single largest *controllable* signal of skill, and it's currently zero.

3. **NO METRICS IN BULLETS.** Every bullet describes *what you did*; none describe *what changed*. Recruiters skim for numbers (% improvement, throughput, scale). Yours has none. The OCR/Docker/multi-DB work is genuinely strong, but the framing makes it look generic.

4. **BROKEN ENGLISH IN BULLET 2.** *"I have experience working on production systems handling real-time workflows..."* — first-person sentence in a third-person bullet list. For a non-native speaker, this anchors the recruiter's read of communication ability. **One sentence, big damage.**

5. **APPLYING TO THE WRONG ROLES.** You reported recruiter-screen rejections of type (i) "we don't sponsor visas." If you're in India applying to India jobs, this should not be happening. Means you're spending cycles on US/EU-only remote roles that don't hire from India. **Wasted effort.**

Order of repair: **(2) GitHub** → **(3+4) Resume rewrite** → **(1) reframe Trainee** → **(5) tighten targeting**. Order matters because resume edits without GitHub artifacts ring hollow.

---

## 3. Real positioning

### Old positioning (current resume)
> *Software Engineer Trainee at Algonox Technologies. CS graduate. Did some Python and Docker work.*

### Real positioning (the truth, sharp)
> **Backend & DevOps engineer with ~1 year of production experience shipping a multi-service OCR/document-intelligence platform. Owns end-to-end deployment across UAT/PreProd/Prod on Linux+Docker. Comfortable with multi-database migrations (Oracle, MySQL, MSSQL) and ABBYY OCR operations.**

This is not exaggeration. It's the same facts framed by *outcome and ownership* instead of by *task list*. It's also exactly what a Tier-B mid-product-company SDE-1 hiring bar looks like.

### One-line elevator answer (memorize, deliver verbatim in screens)
> *"I'm a backend engineer with about a year of production experience at a Hyderabad document-AI company. I own deployments across UAT, PreProd, and Production for a multi-service OCR pipeline — Python, Docker, Linux, Oracle and MySQL — and I built the document-skew preprocessing layer that fixed extraction accuracy on rotated scans. I'm looking for an SDE-1 backend role at a product company where I can keep working on real systems."*

~30 seconds. Strong. Specific. No "trainee" in it. No apology. Practice it until you can deliver it without thinking. **This single sentence is your highest-leverage interview asset.**

---

## 4. Target archetype — exactly what to apply for

### Job titles to filter on
- Software Engineer (SDE-1 / SE-1 / Associate Software Engineer)
- Backend Engineer / Backend Developer
- Python Developer (when senior=0–2 yrs)
- Junior Software Engineer
- Graduate Engineer Trainee (GET) — at product companies only, not service body-shops
- Software Development Engineer I

### Job titles to AVOID
- "Senior" anything (will be rejected at screen)
- "Lead" / "Tech Lead" (same)
- Pure frontend (you don't have JS depth — wastes screens)
- Data Scientist / ML Engineer (needs different stack signal)
- Full-stack at product companies (your JS isn't deep enough; you'll get burnt at tech screen)

### Geography filter
- Hyderabad (primary)
- Bangalore / Pune / Chennai / NCR (only if remote-OK or you'd relocate)
- Remote India only (NOT remote global — those almost never hire from India in the timeframe)
- Reject: anything requiring passport/visa/travel

### Company tiers (where to spend effort)

**Tier B — primary target (60% of effort, ~80–100 apps over 4 weeks)**
*Mid-tier product / well-funded startup, hires from non-IIT colleges, ₹6–12 LPA*

Hyderabad-based or strong Hyderabad presence:
- Darwinbox, Highradius, Postman, Hasura, Zluri, ToTheNew, Cyient, Pegasystems
- Razorpay, PhonePe, CRED, Slice, Groww, Zerodha (Bangalore but remote-friendly)
- Freshworks, Chargebee (Chennai, remote-friendly)
- Innovaccer, Locus, Druva, Whatfix, BrowserStack
- Apollo 24/7, Practo, MFine (healthtech, often hiring backend)
- Skyflow, Sprinklr Hyderabad
- T-Hub residents — see [https://t-hub.co](https://t-hub.co) startup directory
- Y Combinator companies hiring from India — see [https://www.workatastartup.com](https://www.workatastartup.com)

**Tier C — safety net (30% of effort, ~50–60 apps)**
*Tier-2 services + mid-IT, predictable pipelines, ₹4–7 LPA*

- Cognizant, LTIMindtree, Persistent Systems, Mphasis, Hexaware, Birlasoft, Coforge
- Capgemini, HCL, Tech Mahindra, Wipro, Infosys (the big ones — slower, but volume helps)
- ValueMomentum, Virtusa, Cyient, Zensar
- Avoid pure body-shops with no product / no real engineering culture (CMC Ltd, etc.)

**Tier A — referral-only stretch (10% of effort, 5–10 referral asks)**
*Big tech, FAANG-tier, ₹14–25+ LPA*

- Microsoft IDC, Amazon Hyderabad, Google, Salesforce, ServiceNow, Atlassian, Qualcomm, Uber, Walmart Labs, DE Shaw, JPMC, Wells Fargo Tech
- Apply *only* through 2nd-degree LinkedIn referrals — direct apps from your profile won't survive ATS at these.

---

## 5. Comp strategy — non-negotiable rules

| Scenario | Rule |
|---|---|
| Recruiter asks current comp | *"I'd prefer to discuss expectations rather than current comp; my current role is a structured trainee program with non-standard pay."* Repeat once if pressed. Never disclose ₹10k. |
| Recruiter asks expected comp | *"I'm looking at market rate for SDE-1 backend in Hyderabad — broadly ₹6–8 LPA fixed, open for the right opportunity."* |
| Offer at ≥ ₹6 LPA fixed | Negotiate hard for ₹7–8. Ask for stock/joining bonus separately. |
| Offer at ₹4.5–6 LPA fixed | Accept if no other live process; negotiate for ₹5+. This is escape velocity. |
| Offer below ₹4.5 LPA | Decline politely. Continue search. |
| Algonox counter-offers FT conversion | Decline anything below ₹6 LPA. They had a year to value you correctly. They didn't. |

**Why ₹4.5 LPA is the floor:** Mathematically, anything lower keeps you in financial fragility. Anything at or above it gives you ~₹30k/month take-home, allows you to start saving, and puts you in a normal-comp position to job-hop again in 12–18 months for the bigger jump.



---

## 6. The 6-week execution plan (day-by-day discipline)

You said "not staying consistent." That stops here. Inconsistency is the largest controllable variable, and it has been killing you for 6 months. The schedule below is non-negotiable. Print it. Stick it to your wall.

### Daily floor (Mon–Fri, while at Algonox) — minimum 3.5 hrs/day on the campaign

| Time | Activity |
|---|---|
| 06:30–07:30 | 1× LeetCode medium (alternating: arrays/strings, trees, graphs, DP). Solution + write notes. |
| 09:00–18:00 | Algonox work (do it well; mine it for resume bullet metrics every Friday) |
| 19:00–19:30 | 5× targeted job applications (resume tailored — see §8) |
| 19:30–20:30 | One of: GitHub repo work / interview prep / mock interview / system-design study (rotates daily — see weekly grid) |
| 20:30–21:00 | LinkedIn: 3 referral asks OR 3 connect-requests with personal note to engineers at target companies |

### Weekend floor — minimum 8 hrs/day

| Saturday | Sunday |
|---|---|
| 4 hrs GitHub project sprint (one of the three repos in §7) | 2 hrs strategy review + plan next week |
| 2 hrs DSA (3× problems, mixed difficulty) | 2 hrs system-design / behavioral prep |
| 2 hrs 1 mock interview (use Pramp / Interviewing.io free tier, or trade with peers) | 4 hrs continue GitHub project sprint |

### Weekly grid — 6-week sprint

#### Week 1 (May 22 – May 28) — **STOP THE BLEED**
- **Goal:** Resume v2 + GitHub Repo #1 live + LinkedIn rewritten.
- **Apps target:** 25 (deliberately low — fix positioning before scaling volume)
- **Outcome metric:** by Sunday EOD, you have a recruiter-ready resume + 1 working GitHub repo with code that proves you can ship.

#### Week 2 (May 29 – Jun 4) — **VOLUME + GITHUB #2**
- **Goal:** GitHub Repo #2 live + 60 applications (Tier B + Tier C mix)
- **Apps target:** 60
- **Referral asks:** 10
- **Outcome metric:** ≥10 recruiter screens scheduled or completed.

#### Week 3 (Jun 5 – Jun 11) — **GITHUB #3 + ACTIVE PIPELINE**
- **Goal:** GitHub Repo #3 live; deepen interview prep; convert recruiter screens → tech screens
- **Apps target:** 50 (drop volume slightly as live pipeline grows)
- **Outcome metric:** ≥3 tech screens scheduled this week.

#### Week 4 (Jun 12 – Jun 18) — **TECH SCREENS / ONSITES**
- **Goal:** Survive tech screens; convert to onsites
- **Apps target:** 40 (replenishment only)
- **Outcome metric:** ≥1 onsite scheduled.

#### Week 5 (Jun 19 – Jun 25) — **CLOSE**
- **Goal:** Onsites + offer negotiations
- **Apps target:** 30 (only if pipeline has room)
- **Outcome metric:** ≥1 offer in hand.

#### Week 6 (Jun 26 – Jul 2) — **NEGOTIATE / SIGN**
- **Goal:** Compare offers; negotiate; sign by Jul 15.
- **Outcome metric:** Signed offer ≥ ₹4.5 LPA fixed.

### Stop-loss / pivot triggers

- **End of Week 2, < 10 recruiter screens:** Resume + GitHub still failing. Re-diagnose, do not just "apply more."
- **End of Week 3, 0 tech screens:** Recruiter-screen narrative is broken. Record yourself doing the elevator pitch and review.
- **End of Week 4, 0 onsites:** Tech-screen execution is the bottleneck. Pause apps for 2 days; intensify DSA + mock interviews.
- **End of Week 5, 0 offers and 0 onsites:** Take any Tier-C offer ≥ ₹4 LPA that comes in Week 6. Escape first; optimize later.

---

## 7. GitHub repair — three repos to ship in 3 weeks

These are personal projects that *demonstrate the same capabilities you have at Algonox*, **without using any Algonox code or IP**. They are recruiter bait: each one is a 30-second click-through that proves you can write working code. README-driven; deployed if possible.

### Repo 1 — `doc-skew-detector` (Week 1 — DO THIS FIRST)
**What:** Python library + CLI that detects skew/rotation in scanned PDF or image documents and corrects it. Mirrors the *concept* of your Algonox preprocessing work; builds with public libraries only.

**Stack:** Python 3.11, OpenCV, pytesseract, PyMuPDF, Click, pytest, Docker.

**Must include:**
- 4 detection methods (projection profile, Hough transform, Tesseract OSD, FFT) with weighted scoring — directly maps to your resume bullet
- Confidence threshold to skip ambiguous pages
- CLI: `doc-skew --input file.pdf --output corrected.pdf --threshold 0.7`
- Dockerfile + `docker-compose.yml`
- README with: problem statement, results table on a public test set (e.g., FUNSD or your own scanned samples), how-to-run, architecture diagram (1 image)
- Pytest suite with ≥10 tests
- GitHub Actions CI: lint + test on push

**Why this repo:** Directly proves the OCR/preprocessing claim on your resume. Recruiter clicks → sees a working tool with measurable accuracy → believes the resume.

### Repo 2 — `multi-db-migrate` (Week 2)
**What:** Python CLI tool that runs idempotent schema + data migrations across Oracle, MySQL, and MS SQL Server with rollback and dry-run support.

**Stack:** Python 3.11, SQLAlchemy core, Alembic, Click, pytest, Docker (with all 3 DB containers in docker-compose).

**Must include:**
- Migration file format (SQL or Python)
- `up` / `down` / `status` / `dry-run` commands
- Pre-migration backup (DDL+data)
- Post-migration sanity-check hooks
- Single docker-compose that spins up Oracle XE + MySQL + MSSQL for local testing
- README with the multi-DB story

**Why this repo:** Directly proves your "multi-DB migrations across Oracle/MySQL/MSSQL" bullet. Most freshers can't even spin up these three DBs locally; doing it well screens you above the median.

### Repo 3 — `pyservice-template` (Week 3)
**What:** Production-grade FastAPI service template — what you'd reach for on day 1 of a new backend job.

**Stack:** FastAPI, Pydantic v2, SQLAlchemy 2.x async, Postgres, Redis, Alembic, structlog, OpenTelemetry, pytest, Docker, docker-compose, GitHub Actions.

**Must include:**
- `/healthz` + `/readyz` endpoints
- Structured logging
- Request-ID middleware
- Configuration via Pydantic Settings + `.env`
- Async DB + caching example
- Dockerfile (multi-stage, non-root)
- docker-compose with API + Postgres + Redis
- 3 example endpoints with full CRUD + tests
- README with architecture diagram + onboarding instructions

**Why this repo:** Shows you can architect a service, not just contribute to one. Sets the expectation that you operate at SDE-1 / mid-junior, not at trainee.

### Repo cosmetics (do this Week 1 along with Repo 1)
- Each repo: clean README with badges, a "What this is" 2-sentence summary, a runnable example, and a screenshot or output sample.
- Pin all 3 repos to your GitHub profile.
- Replace your profile README with a shorter version that links the 3 pinned repos prominently. The current README's narrative is fine but the repos must come first.

---

## 8. Resume rewrite

A complete v2 resume is committed alongside this document as `resume/resume-v2.md`. Read it. Edit metrics where you have real numbers (% accuracy improvement, query count, deployment frequency). Compile to PDF and use this version for *all* future applications.

Key changes from v1:
1. Title presented as **"Software Engineer — Trainee Program"** instead of "Software Engineer Trainee (Temporary)". Same role, sharper framing. Not a lie.
2. Bullet 2 (broken English) deleted; replaced with metric-bearing bullet.
3. Every bullet now starts with strong verb + outcome.
4. Spotify project replaced by the 3 personal projects (as they ship).
5. Skills section reorganized: Backend (primary), Databases, DevOps, Languages — frontend (HTML/CSS/JS) demoted to one line. Targets backend recruiters.
6. Top "Summary" line added (3 lines) — what you are, what you've shipped, what you're looking for.

---

## 9. LinkedIn rewrite

| Section | Action |
|---|---|
| Headline | `Backend & DevOps Engineer · Python · Docker · OCR & Document Intelligence · Open to SDE-1 roles in Hyderabad` |
| About | First paragraph: 3 lines of positioning (same as resume Summary). Second paragraph: 1 sentence on each of the 3 GitHub projects with links. |
| Featured | Pin the 3 GitHub repos as featured links. |
| Experience: Algonox | Mirror the resume v2 bullets exactly. |
| Open To Work | Turn ON, set to recruiters-only (so Algonox doesn't see). Roles: SDE-1 / Backend Engineer / Python Developer. |

### Outreach playbook (5 messages/day, M–F)
- Find target company (Tier B). Find *engineers* in similar role (not recruiters first).
- Message template — short, no flattery, no resume dump:

```
Hi [Name],

I'm a Python/backend engineer ~1 year in, currently shipping
production OCR services at Algonox in Hyderabad (Docker, multi-DB
migrations, Linux deployments). I'm exploring SDE-1 roles and your
team at [Company] caught my eye because [one specific reason — read
their engineering blog or one product feature].

Would you be open to a 15-minute chat about engineering at
[Company]? Happy to share my GitHub if useful.

— Raviteja
```

Reply rate target: 10–15%. So 5/day × 5 days = 25 outreaches/week → 3–4 conversations/week → 1–2 referrals/week. Compounds fast.

---

## 10. Interview prep — what to drill

### DSA (your weakest pillar based on tech-screen leak)

Daily 1× medium. Patterns to drill in this order (pick one per day):
1. Arrays / two-pointer / sliding window
2. Strings
3. Hashmaps / sets
4. Trees (BFS/DFS, recursion)
5. Graphs (BFS/DFS, Union-Find)
6. Linked lists
7. Stacks / queues / monotonic stack
8. Binary search
9. Recursion / backtracking
10. Dynamic programming (1D → 2D)

Use NeetCode 150 as the curriculum. Track in a spreadsheet — problem, pattern, time-to-solve, did-I-need-hint, revisit-date. Re-solve every "needed hint" problem after 3 days, then 7, then 14.

### System design (light prep — SDE-1 doesn't usually deep-dive but might touch)
- Read: *System Design Primer* (GitHub donnemartin/system-design-primer) — at minimum the "Design a URL shortener" and "Design a notification system" sections.
- Be able to whiteboard: REST API + DB schema + caching + retry/queue for one of: file upload service, notification system, URL shortener.

### Behavioral (STAR format, 6 stories)
Draft 2-minute STAR answers for these 6 prompts. Memorize the structure, deliver naturally:
1. Tell me about a production bug you debugged.
2. Tell me about a deployment that went wrong.
3. Tell me about a time you had to learn a new technology fast.
4. Tell me about a time you disagreed with a teammate / lead.
5. Why are you leaving Algonox?
6. Where do you see yourself in 2 years?

For (5), the answer is **never** "the pay is too low" or "they won't convert me." It is:
> *"My current role has been a strong learning experience, especially on the deployment and DB-migration side, but it's structured as a trainee program. I'm ready to take on a full-time SDE role with broader scope and ownership at a product team."*

That's the truth, framed maximally.

---

## 11. The Algonox question — when and how to leave

**Now:** Stay employed. Income > 0 still > ₹10k after fixed costs. **Do not quit until you have a signed offer in hand.** Quitting now = zero income + zero leverage in interviews ("why did you leave with nothing lined up?").

**Have you asked them for FT conversion?** You haven't told me. Do this once, in writing (email, not chat), before end of Week 2:

> "Subject: Discussion — Full-time conversion
>
> Hi [Manager],
>
> I've been with Algonox for 11 months as a trainee, working on production OCR systems and multi-environment deployments. I'd like to discuss converting to a full-time engineering role with a corresponding compensation review.
>
> Could we schedule 30 minutes this week or next?
>
> Thanks,
> Raviteja"

**Reasons:**
1. **Information.** Their answer tells you everything about the company. Yes-with-fair-comp = a real option. Yes-but-₹3-LPA = confirms exploitation, removes guilt about leaving. Vague-non-answer = leave faster.
2. **Optionality.** A counter-offer at decent comp is leverage with new employers ("I have a ₹6 LPA conversion on the table").
3. **Ethics-clear.** You asked. They had the chance. Whatever happens after is on them.

**When you sign elsewhere:**
- Standard 30-day notice (or whatever your contract says — read it).
- Polite resignation email. Do not burn the bridge — Hyderabad's startup scene is small.
- Ensure no IP/code from Algonox is in your GitHub repos.

---

## 12. What we will NOT do (and why)

These are tempting "AI job platform" features that will burn your time, your reputation, or both. They are explicitly killed:

- ❌ **Auto-applying to jobs.** Hurts conversion. Some ATS detect and blacklist.
- ❌ **LinkedIn scraping / mass connect bots.** LinkedIn bans accounts; your professional brand is your only asset.
- ❌ **Mass cold-email recruiters.** CAN-SPAM-equivalent under Indian IT Act + violates etiquette. Manual targeted reach-out at 5/day will outperform 500 spam emails.
- ❌ **Resume "AI optimization" that fabricates skills.** Get caught once, get blacklisted forever. Indian tech community is small.
- ❌ **Buying premium services like LinkedIn Premium / Naukri Premium right now.** Save the money. They don't move conversion at this stage.
- ❌ **More than 3 GitHub projects in 6 weeks.** Three deep > ten shallow. Recruiters look at one. Make it good.
- ❌ **A complex AI job-acquisition platform.** That's later, if at all. Strategy + execution discipline > tooling. We will discuss minimum useful tooling AFTER this strategy is in execution.

---

## 13. Success criteria — when this strategy is "done"

- [ ] `resume/resume-v2.md` published, PDF exported, used for all new applications
- [ ] LinkedIn rewritten per §9
- [ ] Algonox FT-conversion email sent (and answer received, in writing if possible)
- [ ] GitHub repo 1 (`doc-skew-detector`) live with passing CI by end of Week 1
- [ ] GitHub repo 2 (`multi-db-migrate`) live with passing CI by end of Week 2
- [ ] GitHub repo 3 (`pyservice-template`) live with passing CI by end of Week 3
- [ ] All 3 repos pinned on profile; profile README updated
- [ ] ≥175 applications submitted (Tier B + C mix), tailored not spray
- [ ] ≥25 referral asks made (LinkedIn DMs)
- [ ] ≥10 recruiter screens completed
- [ ] ≥3 tech screens completed
- [ ] ≥1 onsite completed
- [ ] **Signed offer ≥ ₹4.5 LPA fixed by 15 Jul 2026** ← the only metric that matters

---

## 14. What's next

This strategy is the foundation. The next conversation determines what (if any) software tooling materially accelerates this plan vs. just being procrastination dressed up in a tech costume.

Candidate tooling — only if it removes friction from THIS plan, not as a portfolio piece:

1. **Application tracker (lightweight CRM)** — record every app, screen, follow-up date, outcome. Accountability tool.
2. **Job aggregator** — pull SDE-1 / backend / Python listings from Cutshort, Instahyre, Wellfound, LinkedIn (legitimate API/RSS only — no scraping). Filter by India-based, ₹4.5 LPA+, junior-level.
3. **Resume tailoring helper** — take base resume + job description, produce a tailored draft in 60 seconds. You review and submit (no auto-apply).
4. **Daily cadence enforcer** — checklist + streak tracker for the daily floor.
5. **Outreach drafting helper** — produce personalized first messages from a target company URL + your base profile.

These are the only candidates. Anything beyond this list is feature theater.

---

**This document is v1. It will be revised at the end of each week's review.**

*Last revised: 22 May 2026.*



---

## 15. Dual-track plan — strategy + `hireloop` as portfolio

*Added 22 May 2026, in response to owner's decision to use the platform itself as the GitHub portfolio piece.*

### Why this works

The original plan called for three small repos (`doc-skew-detector`, `multi-db-migrate`, `pyservice-template`) to repair the GitHub gap. A **single, deeply-built personal job-acquisition cockpit** outguns that — *if* scope stays disciplined. It gives a coherent recruiter narrative:

> *"I built `hireloop` to escape an exploitative trainee role. It is the cockpit I used for this job hunt. Pipeline tracker + AI resume tailoring + daily cadence enforcement. FastAPI, Postgres, pgvector, Next.js. ~5,000 lines. Deployed on Fly.io. Want to see it?"*

That is a hire-worthy story for an SDE-1 / backend role at any Tier-B Indian product company.

### Scope discipline (non-negotiable)

V0 ships **3 features only**: Application CRM, AI Resume Tailoring, Daily Cadence. The 30+ features the original prompt asked for are explicitly killed in the repo's [README](./hireloop/README.md) and [ADR 0003](./hireloop/docs/adr/0003-no-scraping-no-autoapply.md). If owner asks to add features mid-build, the answer is no until V0 ships and is in daily use.

### Time budget

This DOES eat into the apply/practice budget. Hard cap:

- **Mon–Fri:** ≤ 1.5 hrs/day on `hireloop` (after the existing 3.5 hr cadence floor in §6 is met)
- **Sat:** 4 hrs `hireloop` (replaces 1 of the 2 GitHub project-sprint slots)
- **Sun:** 2 hrs `hireloop` (in addition to existing strategy/review block)

If `hireloop` is not on track at end of Week 2 (foundation + applications CRUD working, deployed), pause it and revert to the 3-small-repos plan from §7. **Stop-loss matters.**

### What lives where

- `hireloop/` — the platform repo (currently a subdirectory; extract to `vallakatlaraviteja/hireloop` before recruiter showcase)
- `hireloop/STRATEGY.md`-equivalent → not duplicated; the owner's hiring strategy stays here in the root `STRATEGY.md`
- `hireloop/docs/architecture.md` — system design
- `hireloop/docs/adr/` — irreversible decisions captured (stack, single-owner, no-scraping policy)

### Dual outcome

When this is done, the owner has:

1. **A working tool that tracks the actual job hunt and shipped tailored resumes against real JDs** — meaning the GitHub repo has *real* commits with real demo data (companies he applied to, tailoring runs that produced offers/screens, etc.). This is irreproducible by any clone.
2. **An offer ≥ ₹4.5 LPA fixed by 15 Jul 2026.** Same primary metric as before. Unchanged.



---

## 16. Updates — 22 May 2026 (after owner answered the outstanding questions)

### 16.1 Algonox — closed-door confirmed

Owner asked the company about FT conversion. They said: **"they don't have projects, that's why they are not considering me."**

**Interpretation (sharp):** Algonox has no incoming project pipeline that justifies a new full-time salary. They will retain owner at ₹10k/month "trainee temporary" rate to keep maintaining what's already running, but cannot convert him to full-time at any reasonable comp. This is not malice; it is a company that genuinely cannot afford to convert him.

**Consequence:**

- **The §11 counter-offer-as-leverage plan is dead.** There is no FT offer to extract from Algonox at any level.
- **The Week-2 FT-conversion email script in §11 is no longer needed.** Skip it; the answer is already known.
- Owner leaves the moment an outside offer is signed, with zero guilt. The company already told him the door is closed.
- Until an offer is signed, owner stays employed (income > 0 still > ₹10k). Do the work. Mine it for resume metrics every Friday. Do not pre-quit.

### 16.2 Role-targeting lock

Owner reported applying for: *Software Engineer · Backend Engineer · Data Analyst · DevOps Engineer · Software Developer.*

**Diagnosis:** Three of those five are synonyms (SE / SDev / BE). Two (Data Analyst, DevOps Engineer) are entirely different roles requiring different stacks. A candidate spread across five identities reads as unfocused on a recruiter screen — which contributes directly to the screen-to-tech-screen leak diagnosed in §2.

**Locked target list (from this point forward, NO exceptions):**

- ✅ Software Engineer / SDE-1 / Associate Software Engineer
- ✅ Backend Engineer / Backend Developer
- ✅ Software Developer
- ✅ Python Developer
- ❌ **Data Analyst** — KILL. Wrong stack (SQL + BI + stats). Wastes screens.
- ❌ **DevOps Engineer** — KILL unless owner can demonstrate Terraform + Kubernetes + AWS-at-depth + monitoring-stack experience (he cannot). Without those, fails tech screens. Reapply at V2 in 12 months after building those skills if interested.

**Filter rule for every JD:** if the role description doesn't read primarily as backend Python work, do not apply. Measure in days that pass without applying to a Data Analyst posting; that's progress.

### 16.3 Comp answer — the screen killer must be fixed today

Owner declined to disclose what comp number he tells recruiters ("my personal number").

**Diagnosis:** Whichever of (a) discloses ₹10k current, (b) has no coherent ask, or (c) gives some other underconfident number, the result is the same — recruiter qualifies him out at the screen, which directly causes the 20% screen-to-tech leak diagnosed in §2.

**Mandatory script (memorize verbatim, deliver every recruiter screen, no exceptions):**

> *Recruiter: "What's your current CTC?"*
> *You: "I'd prefer to focus on the role and expectations. My current role is a structured trainee program with non-standard pay; it's not a benchmark for my next role."*

> *Recruiter: "What are you looking for?"*
> *You: "Market rate for SDE-1 backend roles in Hyderabad — broadly ₹6–8 LPA fixed, open for the right opportunity."*

**If pressed a third time on current CTC:** *"It's a trainee stipend, not a salary; I'd rather discuss what your team pays a junior backend engineer."*

**Floor still ₹4.5 LPA fixed.** Ask still ₹6–8. Never volunteer ₹10k. Never accept "tell me your number first" — answer with the script above and pivot.
