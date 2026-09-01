# Fit Assessment Procedure

This procedure produces a single `fit_score` (an integer from 1 to 10) for a
specific role, plus a short written assessment. It is loaded by the
`start-application` skill at Stage 1, and its gap-interview guidance is used at
Stage 2.

---

## 1. Get the job description

You cannot score a role without its full job description. Get it before doing
anything else.

1. If the user pasted the description text, use it directly.
2. If the user gave a URL:
   - If the URL is on an applicant tracking system known to embed the job
     description inside an iframe (iCIMS, Workday, and similar), do not try a
     plain page fetch. Use a browser tool: navigate to the page, then scroll and
     screenshot the description section, batched into as few calls as possible.
   - Otherwise, fetch the URL. If the page loads, extract the full description
     text.
   - If the page is blocked, returns a login wall, returns a client-rendered
     shell with no description text, or returns a 403, tell the user the page was
     not accessible and ask them to paste the description text. Do not guess and
     do not score a partial description.
3. If a description is only partially available, extract what you can, then ask
   the user to fill any gap in the role title or the core requirements before
   scoring.

---

## 2. The fact source

Score the role against what is *verified* about the candidate, in this order of
precedence:

1. `master-facts.md` in the working directory, if it exists. This is
   authoritative. Pay particular attention to its preferences-and-constraints
   section and its gaps or known-limitations section.
2. The candidate's current resume, if provided.
3. Explicit statements the candidate made in this conversation.

Never score a dimension higher on the basis of experience the candidate has not
verified in one of those three places. An unverified match is a gap, and it feeds
Stage 2.

---

## 3. The rubric

Score each dimension from 1 to 10, then take the weighted average. Weights are the
defaults below. If the candidate's `master-facts.md` preferences-and-constraints
section states a different weighting, that overrides the defaults; note the
override in your output.

| # | Dimension | Weight | Scoring guidance (1 = no fit, 10 = ideal) |
|---|-----------|--------|-------------------------------------------|
| 1 | Level and scope match | 20% | Team and organization size, reporting line, and budget or P&L expectation in the job description versus the candidate's verified scope. Score low when the job description expects accountability the candidate has never held (for example P&L ownership when the candidate has managed delivery but not a budget). |
| 2 | Core-responsibility match | 20% | Does the day-to-day work the job describes match what the candidate does well and wants to do? A responsibility the candidate has explicitly ruled out in their master facts (for example hands-on coding for a leadership role) scores this dimension low even when every other dimension fits. |
| 3 | Domain and industry overlap | 15% | Overlap between the job's industry, sector, and problem domain and the candidate's verified domain experience. |
| 4 | Skills and technical match | 15% | Coverage of the job's named skills and technologies by verified, hands-on or management-level experience. A technology the job centers on that the candidate cannot verify lowers this score and becomes a Stage 2 question. |
| 5 | Trajectory fit | 10% | Is this a realistic next step, a stretch, or a backward step, given the candidate's verified trajectory? |
| 6 | Compensation and benefits | 10% | The posted salary range and benefits versus the candidate's stated targets in their master facts. If the top of the posted range is below the candidate's stated floor, score this dimension very low and flag it in the written assessment. Never repeat a confidential floor figure in any outward-facing text. |
| 7 | Location, work arrangement, and travel | 10% | Remote, hybrid, or onsite; the office location; and the travel expectation, each versus the candidate's constraints in their master facts. |

---

## 4. Compute the result

1. Take the weighted average of the seven dimension scores, using the weights as
   decimals (0.20, 0.20, 0.15, 0.15, 0.10, 0.10, 0.10), and round to the nearest
   integer. (Equivalently: multiply each 1-to-10 score by its decimal weight, sum
   the seven products.) That integer is the `fit_score`.
2. Assign a band:
   - `fit_score` 8, 9, or 10: **Strong**
   - `fit_score` 6 or 7: **Moderate**
   - `fit_score` 4 or 5: **Weak**
   - `fit_score` 1, 2, or 3: **Poor**

---

## 5. The written assessment

Alongside the score, write three short sections:

- **Strengths:** what genuinely lines up, drawn only from verified facts.
- **Gaps and risks:** every dimension that scored low, named plainly. Do not let a
  job title imply scope the candidate has not held. Do not invent concerns that
  the source material does not support.
- **Verdict:** two or three sentences. Is this worth pursuing, and if the score is
  Moderate or below, what specifically would need to be true for it to be worth
  pursuing anyway?

---

## 6. Hard stops

If the role trips a sector or values exclusion the candidate has documented in
their master facts, stop at Stage 1. State the specific exclusion and do not score
the remaining dimensions. Apply judgment rather than a keyword filter: a general
diversity statement is not the same as a company whose central purpose is one the
candidate has ruled out.

---

## 7. Gap-interview guidance (Stage 2)

Run a gap interview only when you scored at least one rubric dimension on an
assumption or an unknown, specifically:

- a skill or technology the job names that is not settled in the fact source
- an ambiguous scope question (team size, reporting line, budget authority) the
  job description does not make clear and the fact source does not answer
- a compensation or logistics question the fact source does not answer

Ask one question at a time. Ask only questions whose answer would change a
dimension score or protect the candidate's credibility in a later application. If
the job description is fully answerable from the fact source, skip Stage 2
entirely.
