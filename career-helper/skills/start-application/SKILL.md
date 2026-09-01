---
name: start-application
description: This skill should be used when the user asks to "assess a role before applying", "should I apply to this job", "start an application", "fit check this posting", "run a fit assessment", or provides a job description or URL and wants to know whether it is worth pursuing. Runs a scored fit assessment against a weighted rubric, interviews the user to close knowledge gaps, records the answers to their master facts file, and on a strong result auto-runs networking intelligence and resume tailoring.
tags: fit, assessment, application, screening, rubric, networking, resume, job-search
---

# Start Application

Decide whether a specific role is worth applying to before you spend effort on a
tailored resume or cover letter. This skill scores the fit, interviews you to
close any gaps in what it knows about you, records those answers to your master
facts file, and on a strong result runs a networking check and tailors your
resume automatically.

## Capabilities

| Stage | What it does | When it runs |
|:------|:-------------|:-------------|
| 1 | Score the role's fit against a weighted rubric (1-10) | Always |
| 2 | Interview you to close a knowledge gap | Only when a dimension was scored on an unknown |
| 3 | Record your answers to `master-facts.md`, with a diff | Only when Stage 2 ran |
| 4 | Gate on the score, and auto-chain to networking and resume on a strong fit | Always (unless a Stage 1 hard stop fired) |
| 5 | Optional: update a local job-search tracker database | Only when `job_search.db` is present |
| 6 | Summarize | Always (unless a Stage 1 hard stop fired) |

## Quick Start

```text
"Should I apply to this role?" [paste job description]
"Fit check this posting: [URL]"
"Start an application for the Director of Engineering role at [Company]"
"Run a fit assessment on this JD"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** -> Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors, use plain replacements. Explicit signposting at every transition ("Stage 2 of 6. Next: recording your answers."). Refer to saved files by description, not filename. Repeat key details (company names, role titles, dates), do not assume the user remembers from earlier messages.
- **colour_blind: true** -> Never use color alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once: "Do you have any accessibility preferences I should know about? For example, if you're dyslexic I can adjust how I format things." If yes, save to `career-helper-preferences.md` using the format documented in the Tim skill before continuing. If the user declines or says no, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## Coaching Voice

Be direct about fit. If the role is a weak match, say so plainly and say why.
Name gaps rather than talking around them: a job title does not prove the scope
behind it, and pretending a gap is not there just moves the problem to the
interview.

Distinguish two things and say which one you are giving:

- *Role analysis:* how well this specific role lines up with the candidate's
  verified experience.
- *Direction advice:* stepping back from this one role, is this the direction the
  candidate wants to be heading?

Address the user as "you". Use the Oxford comma. Never use em dashes.

---

## Stage 1: Score the fit

Load `@references/fit-assessment.md` and follow it:

1. Get the job description (its section 1).
2. Identify the fact source (its section 2): `master-facts.md` in the working
   directory if present, otherwise the current resume plus what the user says.
3. Score all seven rubric dimensions and compute the weighted `fit_score` and
   band (its sections 3 and 4).
4. Write the strengths, gaps and risks, and verdict (its section 5).
5. Apply the hard stops (its section 6). If a stop fires, report it and end here.

If your runtime provides a task-list tool, keep a list of Stages 1 to 6 and
update it as you go.

Present the score, band, and written assessment to the user before continuing.

## Stage 2: Interview to close gaps

Follow the gap-interview guidance in `@references/fit-assessment.md` section 7.
Run this stage only when you scored a dimension on an assumption or an unknown.
Ask one question at a time. If the job description was fully answerable from the
fact source, skip to Stage 4.

## Stage 3: Record answers to master facts

For each answer the user gave in Stage 2, integrate it into the correct existing
section of `master-facts.md`:

- a technology or depth clarification -> the technical-depth or skills section
- an achievement or metric -> the achievements section
- a preference, constraint, or logistics fact -> the preferences-and-constraints
  section
- a newly confirmed fact not yet on the resume -> the confirmed-facts section
- a limitation or caveat -> the gaps or known-limitations section

Follow the plugin's verified-content rules: add no invented detail, favor
accuracy over embellishment, never inflate a metric, use US spelling, and use no
em dashes in the prose you add.

**Show the user a diff of every change to `master-facts.md` before continuing.**

If no `master-facts.md` exists, offer to create one from
`@../application-optimizer/references/master-facts-template.md`. If the user
declines, keep their answers in this conversation and in the Stage 4 output
document only.

After editing, re-run the Stage 1 scoring with the new facts and report the
updated `fit_score`. Re-score only; do not run Stage 2 again even if the new
facts appear to raise fresh questions.

## Stage 4: Gate and auto-chain

First, write the assessment to `applications/{role-slug}-{company-slug}/fit-assessment.md`
using `@references/fit-assessment-template.md`. Do this regardless of the gate
outcome. Follow the slug convention already in use in the `applications/` folder
(look at a couple of existing folders first); use `{company-slug}` alone when the
role title is generic.

Then gate on `fit_score`:

- **8 or higher (Strong):** run both chain steps below, in order, without pausing.
- **6 or 7 (Moderate):** present the full assessment and ask the user whether to
  proceed. On yes, run both chain steps without further pausing. On no, go to
  Stage 5.
- **5 or lower (Weak or Poor):** stop. Report the assessment and the main
  reasons. Do not run the chain. Offer the user the Stage 5 logging step so the
  assessment can still be recorded.

If a reference file a chain step needs (`career-navigator` or
`application-optimizer` under `../`) cannot be found, report which file is
missing and stop the chain. The Stage 1 to 3 assessment and the
`fit-assessment.md` file are still delivered.

### Chain step 1: Networking check

Load `@../career-navigator/SKILL.md` and
`@../career-navigator/references/networking-intelligence-template.md`. Run
Capability 1 (Strategic Networking) for this company and role. Save the output to
`applications/{slug}/networking-intelligence.md`.

### Chain step 2: Resume tailoring

> **Temporary bridge (deviation D1).** Resume `.docx` production has not yet been
> migrated into this plugin. Until it is:

- If a `job-application-assistant` skill is available in this environment (check
  for `.claude/skills/job-application-assistant/SKILL.md` in the working
  directory or any loaded plugin), run its Task 3, "Customizing the Resume for a
  Specific Role", end to end, reusing the job description already fetched in
  Stage 1.
- Otherwise, load `@../application-optimizer/SKILL.md` and run
  `application-optimizer`'s resume/ATS Optimization capability (Capability 2),
  reusing the same job description, and its Document Output capability
  (Capability 6) if a `master_resume_docx` is recorded in
  `career-helper-preferences.md`.

## Stage 5: Job-search tracker integration (optional)

> **Optional integration (deviation D2).** This stage self-skips when it does not
> apply. A plain career-helper user with no local tracker database is unaffected.

Check for `job_search.db` in the working directory.

- **Not present:** skip this stage silently.
- **Present:** look up the role:
  `SELECT id, status FROM opportunities WHERE company = ? AND title = ?`
  (parameterized; use the `sqlite3` command, or Python's `sqlite3` module if the
  command is not available).
  - If `job_dashboard/db.py` is not present alongside the database, report that
    the tracker helper was not found and skip the write.
  - If the `SELECT` returns more than one row, do not write. Show the user every
    matching row (id, title, company, status) and ask which one to update, or
    whether to skip the database step.
  - On the Weak or Poor path (Stage 4 gate <= 5), ask before writing.
  - **A row exists:** update `fit_score` (integer 1-10) and `fit_reason` (the
    verdict prose) via `job_dashboard/db.py`'s
    `update_row(conn, row_id, fields)`, passing `fields` as a dict of strings. Do
    not change the row's `status`.
  - **No row exists:** ask the user whether to add one. On yes, create it via
    `job_dashboard/db.py`'s
    `create_row(conn, fields, allowed_statuses=OPPORTUNITY_STATUSES)` with status
    `New` and fields for `fit_score`, `fit_reason`, `title`, `company`,
    `link_url`, and a `notes` value pointing at the `applications/{slug}/`
    folder. On no, leave the database untouched.
  - `create_row` returns a `(row, errors)` tuple, and it (or its internal row
    lookup) can raise even when the INSERT and commit already succeeded. A raised
    exception or a falsy return is therefore not proof the insert failed.
  - After any write, re-query the affected row (a `SELECT` by `company` and
    `title`, or by id) to confirm the write landed before reporting success. If
    the re-query does not reflect the write, treat it as failed and report it; do
    not retry a write that the re-query shows already landed, because that creates
    duplicate rows.

## Stage 6: Summarize

Report:

- the `fit_score` and a one-line verdict
- what was added to `master-facts.md`, or that nothing was
- the `applications/{slug}/` folder path and the files now in it
  (`fit-assessment.md`, and when the chain ran, `networking-intelligence.md` plus
  the tailored resume)
- the tracker-database outcome, if Stage 5 ran
- when the chain ran the resume step through `job-application-assistant` Task 3:
  that a cover letter and an application-log entry were **not** produced, because
  those are separate requests

---

## Related Skills

- **/application-optimizer** - Company research, ATS resume rewriting, cover letters
- **/career-navigator** - Networking, job search planning, offer evaluation, application tracking
- **/interview-master** - Interview preparation and post-interview coaching

---

*Start Application v1.0.0 | Career Helper Plugin | Prosper AI Consulting*
