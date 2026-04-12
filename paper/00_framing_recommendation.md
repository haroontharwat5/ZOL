# Framing Recommendation for the ZOL OR Efficiency Paper

**For:** Haroon Tharwat — before the meeting with Niels Martin & Maxim Riebus
**Date:** April 2026
**Status:** Draft recommendation — meant to be debated, not followed blindly

---

## TL;DR

I recommend we frame the paper as a **natural experiment in operating-room benchmarking**: four sites (Genk, Maaseik, Lanaken, Cathlab) share the same governance, EHR, and ownership, yet run four structurally different OR operating models. Their raw overtime rates differ by **16.8×** (Lanaken 0.5% vs Genk 8.4%), and the paper's central contribution is to show that this kind of raw spread is almost entirely **operating-model artifact** — a warning to anyone who benchmarks OR performance at the hospital level without adjusting for what the hospital actually *is*.

This framing is honest to the data, is methodologically original, and targets a Q1 healthcare-operations audience (**Health Care Management Science**) rather than a surgery audience (BJS).

---

## 1. Why I am *not* recommending our original BJS outline

The BJS outline framed this as a surgery paper: "planned vs actual times, start delays, overtime, room swaps." That framing has three problems:

1. **It isn't surgical.** BJS and similar surgery journals want clinical outcomes, not process metrics. Our dataset has no morbidity, mortality, or readmission data. Reviewers would ask: "so what does this mean for patients?" and we would have no clean answer.
2. **The numbers don't support a single-metric story.** The most dramatic finding — 16.8× spread in overtime — is almost entirely explained by case mix and operating model. If we sell that number as a quality gap, a careful reviewer will dismantle the paper.
3. **The most interesting thing in the data is not any single metric — it's the *methodology* of comparing four operating models under shared governance.** That belongs in a management/operations journal, not a surgery journal.

## 2. The three framings I considered

### Framing A — "Process drivers of OR inefficiency" (two-lever)
**Claim:** Duration-estimation accuracy is similar across sites; what differs is start-time discipline and delay cascading. Sites that cascade end up with more overtime.

**Strengths:** Clean mechanism. Ties in well with the existing literature on first-case on-time starts (Dexter & colleagues).
**Weaknesses:** After our in-depth review, the data don't cleanly separate "prediction" from "process." Duration CVs *do* differ across sites, just less than overtime rates do. And first-case punctuality does not monotonically rank the sites in the order their overtime rates do. So the claim "process >> prediction" is only partly true, and a reviewer would call us on it.

### Framing B — "Within-campus room heterogeneity is larger than between-campus variation"
**Claim:** Benchmarking hospitals at the aggregate level hides the fact that most of the variance lives inside the hospital, between rooms. At Lanaken (a small site), the worst-performing room has ~16× the overtime rate of the best. At Maaseik, ~35×.

**Strengths:** Genuinely novel finding. Actionable (room-level improvement beats hospital-level improvement).
**Weaknesses:** Hard to tell as a standalone story because the reader first asks "why should I care about within-campus variation?" We still need the raw between-campus spread as the hook.

### Framing C — "A natural experiment across four operating models" *(RECOMMENDED)*
**Claim:** Under shared governance, the four ZOL sites operate four distinct OR business models (high-volume ambulatory flex, mid-sized inpatient-heavy, complex 24/7, and specialized interventional). Raw metrics rank them in a misleading order; progressive stratification shows that most of the spread is model artifact; what's left sits inside rooms. Therefore OR benchmarking must adjust for *operating model*, not just case mix.

**Why I think this wins:**
- It uses *every* piece of data we have and turns each finding into part of a single argument.
- It is genuinely original: I could not find a published paper that treats a hospital network as a natural experiment in operating-model design with this kind of progressive stratification analysis.
- It is the right level of ambition for a Q1 management journal. BJS and JAMA Surgery would not know what to do with it; Health Care Management Science is exactly its audience.
- It sidesteps the "so what does this mean for patients?" trap by focusing on the decision-makers who actually use OR efficiency metrics: operations managers and benchmarking consortia.

## 3. What this framing buys us in the results section

Every piece of completed analysis becomes a beat in the argument:

| Finding | Role in the paper |
|---|---|
| 16.8× raw overtime spread (Genk 8.4% vs Lanaken 0.5%) | Hook — "naive benchmarking makes Lanaken look 16× better than Genk" |
| Lanaken is 98% ambulatory day cases, Genk is 58% inpatient | First stratification — the gap shrinks |
| Lanaken has no weekends, Genk runs 24/7 | Second stratification — shrinks further |
| Cathlab is actually 88.6% **inpatient**, not ambulatory (fixing a documentation error in our own in-depth report) | Integrity check — we verify our data before comparing |
| Residual 3–4× spread after full stratification | The "honest" benchmarking number |
| Within-room variation at Maaseik ≈ 35× and at Lanaken ≈ 16× | The bigger lever than between-hospital ranking |
| LP01↔LP02 paired-room flex: 100% bidirectional swaps; 7.5% swap rate overall | Operating model finding — flex is a design, not a failure |
| GO11 at Genk: 90% late starts, mean +320 min, but average overtime | Operating model finding — this room is a "network valve" absorbing urgent demand |
| Duration CV by planned-length bucket is similar across sites | Rules out "some sites are just better at estimation" |
| Shift-transition compression (cases crossing shift boundaries finish shorter than planned) | Novel mechanism, explains the P95 overtime tail |

Every finding earns its place.

## 4. What this framing gives up

Three things we won't be able to claim:

1. **Causality.** We cannot say "if you adopt Lanaken's operating model, your overtime will drop." We can only show that the raw spread is model artifact and that within-model room-level heterogeneity is the bigger lever.
2. **A single hero metric.** "Overtime rate" stops being the headline number and becomes one of several stratified metrics. This is actually correct — the headline is the *methodology*, not the number.
3. **Clinical implications.** We explicitly do not claim anything about patient outcomes. The paper is about operations, not care quality.

## 5. Target journal

**Primary: Health Care Management Science** (Springer, Q1 in Health Policy & Services)
- Impact factor ~3.0, acceptance rate ~25%
- Scope: "applications of operations research and management science to healthcare"
- Recent papers in OR planning, OR scheduling, operating-model comparisons
- Article length: 25–40 pages, tolerates observational studies

**Backup 1: Operations Research for Health Care** (Elsevier)
- Narrower OR focus, IF lower, but tighter audience fit
- Useful if HCMS rejects us on novelty

**Backup 2: BMC Health Services Research**
- Broader scope, open access, high acceptance rate, higher page limit
- Would take it on the empirical strength alone; less prestigious

I recommend submitting to HCMS first and using BMC-HSR as a second-tier fallback. I *do not* recommend BJS or the surgery journals.

## 6. What I need from you and Niels

Three decisions at the Wednesday meeting:

1. **Framing C vs an alternative I haven't thought of.** If Niels has strong reasons to prefer a different frame, I want to hear them now, not after I've written the full draft.
2. **Journal target.** HCMS vs alternative. I have a strong opinion but this is a team call.
3. **What to do about the Cathlab labeling error.** Our in-depth report for Cathlab says "Ambulatory admissions represent 88.6%" but the underlying Table 4 clearly shows HOS (inpatient) = 88.6% and DAG (ambulatory) = 11.3%. **The text is wrong; the table is right.** I recommend we fix this in the report before the paper goes out and include a one-sentence note in the paper's methods section about verifying admission-type labels against the original Dutch codes. This is a trivial fix but we should own it explicitly.

## 7. What this document is for

This is a living document. If the framing changes after the meeting, I will update it in place and keep the revision history in git so we can trace why we chose what we chose.

---

*Next files in this folder:*
- `01_journal_outline.md` — HCMS outline matching this framing
- `02_paper_draft.md` — full draft we'll edit together
- `03_plain_english.md` — the paper in simple language so you can explain it at a dinner table
- `04_advisor_walkthrough.md` — how to present this to Niels and Maxim, section by section
- `05_glossary.md` — every term of art used in the paper, defined
- `06_literature_review.md` — citations and state of the art
