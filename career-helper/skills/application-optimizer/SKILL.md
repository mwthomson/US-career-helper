---
name: application-optimizer
description: This skill should be used when the user asks to "optimize my resume", "fix my resume", "improve my resume", "tailor my resume for ATS", "research a company", "help me apply for a role", or "plan my application". Provides ATS-optimized resume rewriting, company and role research with parallel intelligence gathering, and application strategy planning.
tags: cv, ats, resume, company, research, application, strategy
---

# Application Optimizer

Research companies, optimize your resume for ATS systems, and plan your application strategy.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Company Research | Before applying or interviewing at a target company |
| 2 | resume/ATS Optimization | Tailoring your resume for a specific role |
| 3 | Application Strategy | Planning your full application approach |
| 4 | Cover Letter | Writing a cover letter, supporting statement, or application message |
| 5 | Master Resume Template | One-time: recording which Word file is your permanent resume template |
| 6 | Document Output (.docx) | Turning a tailored resume or cover letter into a .docx that preserves your template's formatting |

## Quick Start

```text
"Research [Company] before I apply"
"Help me optimize my resume for this job description"
"Plan my application to [Company] for [Role]"
"Write a cover letter for this role"
"Help me with the supporting statement for this application"
"Save my tailored resume as a docx using my resume template"
```

---

## Accessibility

**At skill start**, check whether `career-helper-preferences.md` exists in the current working directory. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** → Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors — use plain replacements. Explicit signposting at every transition ("Step 2 of 4. Next: resume optimization."). Refer to saved files by description, not filename. Repeat key details (company names, role titles, dates) — do not assume the user remembers from earlier messages.
- **colour_blind: true** → Never use color alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once — "Do you have any accessibility preferences I should know about? For example, if you're dyslexic I can adjust how I format things." If yes, save to `career-helper-preferences.md` using the format documented in the Tim skill before continuing. If the user declines or says no, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## 1. Company & Role Research

**What you need:** Company name, job description (optional but helpful)
**Before running:** Check whether `applications/{role-slug}/research-brief.md` exists.
If it already exists, skip this capability and reuse the existing brief -- only run
fresh research when no brief exists yet for this role-slug.
**Load:** @references/company-research.md
**Template:** @references/research-brief-template.md

Agentic parallel research covering:
- Company fundamentals, leadership, financial health
- Market position, competitors, strategic direction
- Culture, employee experience (Glassdoor analysis)
- Hiring context and team structure
- People intelligence (hiring manager, key stakeholders)
- Red flags and risk assessment

Uses parallel WebSearch, WebFetch, and Task tool for comprehensive intelligence.

**Output:** `applications/{role-slug}/research-brief.md`

---

## 2. resume Optimization for ATS

**What you need:** Your current resume + target job description
**Load:** @references/ATS-Helper.md
**Templates:**
- @references/cv-template.md for resume output
- @references/application-strategy-template.md for LinkedIn sync notes

NLP and recruitment AI specialist approach:
- Keyword and concept extraction from job description
- ATS-safe resume rewrite with quantified achievements
- Keyword coverage analysis (target: 70%+ of JD terms)
- LinkedIn API consistency checks
- Formatting and parsing safety verification

**Output:**
- `applications/{role-slug}/cv-optimized.md`
- `applications/{role-slug}/linkedin-updates.md` (LinkedIn sync recommendations)

If a `master_resume_docx` is recorded (see Capability 5) or the user wants to set one
now, also produce a `.docx` via Capability 6.

---

## 3. Application Strategy & Timeline

**What you need:** Research brief + optimized resume + timeline constraints
**Template:** @references/application-strategy-template.md

Comprehensive planning:
- Timeline and milestone planning
- Stakeholder mapping and connection strategy
- Risk mitigation for identified gaps
- Follow-up protocols and decision framework
- Cover letter approach (for a full draft, use Capability 4)

**Output:** `applications/{role-slug}/application-strategy.md`

---

## 4. Cover Letter & Supporting Statement

**What you need:** Job description + your resume (or master facts) + research brief if one exists + your own reasons for wanting the role
**Load:** @references/cover-letter.md
**Template:** @references/cover-letter-template.md

Drafts a cover letter, competency-based supporting statement, or short application message, with every claim traceable to verified content:
- Confirms which format the application actually requires before drafting
- Mirrors job-description language only where the underlying fact genuinely matches
- Sources motivation from you, never inventing reasons you care about the organization
- Addresses overqualification, career change, or gaps honestly where the resume cannot
- Runs the same anti-hallucination guardrails and reflective validation as resume work

**Output:**
- `applications/{role-slug}/cover-letter.md` (full letter)
- `applications/{role-slug}/supporting-statement.md` (competency-based applications)

If the user supplies a cover-letter Word template, also produce a `.docx` via
Capability 6.

---

## 5. Master Resume Template

**What you need:** An existing Word (`.docx`) resume you want to reuse as your permanent structural template
**Load:** nothing extra — this capability only manages a preference, not a document

Runs automatically, once, the first time Capability 2 produces a `cv-optimized.md`
and no `master_resume_docx` is recorded yet:

- Checks `career-helper-preferences.md` in the current working directory for a
  `master_resume_docx` path.
- If missing, asks: "Do you have a Word (.docx) resume you'd like to use as your
  permanent template? I'll reuse its exact formatting every time I tailor a resume
  for you, rather than generating a new layout from scratch." (Consent-first, same
  pattern as the accessibility preferences.)
- If the user provides a path, confirms the file exists and is a `.docx`, then saves
  it to `master_resume_docx` in `career-helper-preferences.md` (creating the file if
  it doesn't exist yet, using the format documented in the Tim skill).
- If the user has no Word resume, or declines: proceeds without one. Markdown output
  (`cv-optimized.md`) remains fully available regardless — this capability only
  unlocks Capability 6's `.docx` output for resumes.
- If a recorded `master_resume_docx` path no longer exists on disk, say so and ask
  for a new path, or fall back to markdown-only for the current run — never fabricate
  a replacement.

**Output:** an updated `career-helper-preferences.md` (no document produced).

---

## 6. Document Output (.docx)

**What you need:** A tailored resume (`cv-optimized.md`) or cover letter
(`cover-letter.md`) already produced by Capability 2 or 4, and a Word template to
preserve — `master_resume_docx` (resume) or a cover-letter template the user supplies
(cover letter)
**Load:** @references/docx-template-output.md

Produces a `.docx` by editing the user's own template in place, never by generating a
new layout from scratch:

- Unpacks the template, maps the tailored markdown content into the matching
  sections of `word/document.xml`, and repacks it following
  `docx-template-output.md` exactly — this avoids two silent corruption causes (zip
  directory entries; `.dotx`→`.docx` template content-type leaks) that LibreOffice
  tolerates but Word rejects.
- Runs the mandatory verification checklist in `docx-template-output.md` before
  presenting the file.
- Never modifies the template's header/contact-info block or overall structure —
  only the content sections the tailoring pass changed.
- Markdown output from Capability 2/4 is unaffected either way; `.docx` is additive.

**Output:**
- `applications/{role-slug}/resume.docx` (+ a rendered PDF)
- `applications/{role-slug}/cover-letter.docx` (+ a rendered PDF)

---

## Application Folder

All role-specific outputs are saved in `applications/{role-slug}/`. When running any capability for a role, check if the folder exists first. If it doesn't, create it when saving the first output. The `{role-slug}` is derived from the role title and company (e.g., "Marketing Manager at Greenfield & Co" becomes `marketing-manager-greenfield`).

---

## Deep Research Validation

All research uses a rigorous multi-cycle validation workflow:
**Load:** @references/deep-research-reflection.md

- **Gap Analysis** - After initial search, identify what's missing
- **Counter-Evidence Search** - Actively search for contradicting information
- **Source Credibility Scoring** - SEC filings > news > Glassdoor > blogs
- **Red Flag Hunting** - Proactively search for negative information
- **Citation Requirements** - All factual claims include source URLs and access dates

## Reflective Validation

After generating content, validate before presenting:
**Load:** @references/reflect-validate.md

**For resume/ATS:** Keyword coverage 70%+? Achievements quantified? ATS-safe formatting?
**For Research:** All claims cited? Sources recent (<12mo)? All sections present?

```
Generate -> Evaluate -> If NEEDS_IMPROVEMENT -> Refine -> Re-evaluate (max 2 iterations -- see reflect-validate.md for the punch-list fallback)
```

---

## Career Stage (Persona)

**At skill start**, check `career-helper-preferences.md` for a `career_stage`
field.

- **If `career_stage` is set:** use it directly. Do not re-scan the conversation
  for persona triggers on this or future runs.
- **If `career_stage` is missing:** determine it from context using the trigger
  table below, or ask once: "Which best describes your current stage: standard
  experienced job search, career returner, early career, board/NED search, or
  fractional/portfolio work?" Save the answer to `career_stage` in
  `career-helper-preferences.md`, creating the file if it doesn't exist yet -- but
  only if the user has consented to preference storage (same consent-first pattern
  as the Accessibility section above: if the user declines storage, proceed without
  creating the file).

| `career_stage` value | Load Reference | Trigger (used only when first determining the value) |
|:--------|:--------------|:------|
| `career-returner` | @references/career-returner-cv-guide.md | User mentions career break, returning to work, layoff, maternity/paternity, illness, caregiving |
| `early-career` | @references/early-career-cv-template.md | User is a graduate, apprentice, school leaver, or has limited professional experience |
| `ned` | @references/ned-cv-template.md | User seeks board roles, NED positions, governor or trustee appointments |
| `fractional` | @references/fractional-cv-template.md | User is going fractional, portfolio, or independent consulting |
| `standard` | (none -- standard capability references only) | None of the above apply |

These persona references supplement (not replace) the standard capability
references. Load both the persona reference and the standard one whenever
`career_stage` is one of the four special values above.

---

## Output Standards

- **US English** throughout (unless non-US role explicitly requires US English)
- **No emojis** - Professional tone
- **Cited sources** - All research includes URLs and access dates
- **Quantified metrics** - Specific numbers, percentages, timeframes
- **ATS-safe** - Simple formatting, conventional headings, consistent dates
- **Never invent data** - Mark missing info as `[MISSING]`

### Tone of Voice
- Address the user as "you", not by name, in coaching and strategy content: "Your resume highlights..." not "Bethan's resume highlights..." — default to second person for warmth and engagement; occasional name use is fine for emphasis. (resumes themselves are naturally written in third person about the candidate)
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability specifies a template, you MUST:
1. Load the template first using @ symbol
2. Follow the template structure exactly
3. Preserve template footers

### Working with Blocked Content

When WebFetch fails (LinkedIn, Glassdoor, paywalled content):
- Ask user to screenshot the page (Read tool processes images)
- Or copy/paste text directly
- Or save as PDF and provide path
- Only request screenshots for critical content (top 3-5 items)

---

## Related Skills

After optimizing your application:
- **/linkedin-coach** - Update your LinkedIn to match your resume
- **/interview-master** - Prepare for interviews at this company
- **/career-navigator** - Build networking strategy and plan your search

---

*Application Optimizer v1.4.0 | Career Helper Plugin | Prosper AI Consulting*
