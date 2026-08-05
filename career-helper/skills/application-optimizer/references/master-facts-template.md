# Master Facts Template

**Purpose:** A single source of truth for your career history, metrics, and pre-verified achievement bullets. Maintain this once, then reuse across every application.

**How to use this file:**

1. Copy this template into your workspace as `master-facts.md`.
2. Fill in only what is verifiable. Leave placeholders (`{{LIKE_THIS}}`) in place for anything you are unsure about. Do not guess.
3. When running application-optimizer, the skill will prefer content from this file over anything else. That means every bullet in your generated resume can be traced directly back here.
4. Update the file whenever you land a new achievement, metric, or role change.

**Why bother:**

- Stops every resume rewrite from drifting or inventing details.
- Lets you reuse pre-verified bullets across applications rather than rewriting from scratch.
- Creates an audit trail: every bullet on your resume traces back to a specific entry here.
- Makes it obvious when something is missing, so you can go find the real answer rather than let the AI fill the gap.

**Important:** If a fact is not in this file, the application-optimizer skill will either ask you or leave a `[MISSING]` placeholder. It will never invent a detail to fill a gap.

---

## 1. Identity and Contact

```yaml
name: {{YOUR_NAME}}
target_titles:
  - {{PRIMARY_TARGET_TITLE}}
  - {{SECONDARY_TARGET_TITLE}}
location: {{CITY_COUNTRY}}
email: {{EMAIL}}
phone: {{PHONE}}
linkedin: {{LINKEDIN_URL}}
website_or_portfolio: {{URL_OR_BLANK}}
```

---

## 2. Career Timeline

List every role in reverse chronological order. Use `MMM YYYY` date format. Mark any gaps explicitly.

```
Employer: {{COMPANY_NAME}}
Location: {{CITY_COUNTRY}}
Dates: {{MMM_YYYY}} to {{MMM_YYYY_OR_PRESENT}}
Title(s): {{TITLE_1}}, {{TITLE_2_IF_PROMOTED}}
Reporting to: {{TITLE_OF_MANAGER}}
Team size managed: {{NUMBER_OR_NONE}}
Budget owned: {{CURRENCY_AMOUNT_OR_NONE}}
Scope (geography, business unit): {{SCOPE}}
```

Repeat for each role. If there is a gap between roles, add a line:

```
Gap: {{MMM_YYYY}} to {{MMM_YYYY}}, {{REASON_IF_YOU_WANT_TO_DOCUMENT}}
```

---

## 3. Verified Metrics Bank

Every number you are willing to put on a resume should appear here once, with context. This prevents a metric from drifting between bullets or being combined incorrectly.

```
- Metric: {{e.g., "Grew weekly newsletter from 40k to 180k subscribers"}}
  Role: {{COMPANY_NAME}}, {{TITLE}}
  Timeframe: {{e.g., "Jan 2022 to Dec 2023"}}
  Source: {{HOW_YOU_KNOW_IT_e.g., "Internal dashboard", "Quarterly report"}}
  Attribution: {{"solo" | "co-led with X" | "team of N"}}

- Metric: {{...}}
  Role: {{...}}
  Timeframe: {{...}}
  Source: {{...}}
  Attribution: {{...}}
```

**Rules for this section:**

- Never combine two metrics into one unless they genuinely refer to the same achievement.
- Attribution matters. "Led" and "co-led" are not interchangeable.
- If a number is estimated or approximate, say so here.

---

## 4. Bullet Library

Pre-written, verified bullets organized by emphasis area. When a job description emphasizes leadership, pull from the Leadership section. When it emphasizes technical delivery, pull from the Technical section. And so on.

Each bullet should follow the pattern: **Action verb + Scope + Tool or method + Metric + Outcome**.

### 4.1 Leadership and People

```
- {{VERIFIED_BULLET_1}}
- {{VERIFIED_BULLET_2}}
- {{VERIFIED_BULLET_3}}
```

### 4.2 Strategy and Positioning

```
- {{VERIFIED_BULLET_1}}
- {{VERIFIED_BULLET_2}}
```

### 4.3 Growth and Commercial Impact

```
- {{VERIFIED_BULLET_1}}
- {{VERIFIED_BULLET_2}}
```

### 4.4 Technical Delivery

```
- {{VERIFIED_BULLET_1}}
- {{VERIFIED_BULLET_2}}
```

### 4.5 Stakeholder and Cross-Functional

```
- {{VERIFIED_BULLET_1}}
- {{VERIFIED_BULLET_2}}
```

**Add your own emphasis areas as needed.** Common additions: Product Management, Data and Analytics, Transformation and Change, Governance and Risk, Customer Experience, Sustainability and ESG.

**Rules for this section:**

- Each bullet must be independently verified and ready to use as-is.
- If you write variants of the same bullet (e.g., a shorter version and a longer version), keep both and label them.
- When application-optimizer selects from this library, it should prefer bullets that already contain the specificity the target role needs, rather than trying to add specificity to a generic bullet.

---

## 5. Education

```
- Degree: {{DEGREE_AND_SUBJECT}}
  Institution: {{UNIVERSITY_NAME}}
  Dates: {{YYYY}} to {{YYYY}}
  Grade (optional): {{e.g., "2:1", "First", "GPA 3.8"}}
```

Repeat for each qualification. Do not add education you did not complete unless you explicitly mark it "in progress".

---

## 6. Certifications and Professional Memberships

```
- Name: {{CERTIFICATION_NAME}}
  Issuer: {{ISSUING_BODY}}
  Year: {{YYYY}}
  Expiry (if any): {{YYYY_OR_BLANK}}
  ID or reference (optional): {{CREDENTIAL_ID}}
```

---

## 7. Projects, Publications, Talks (Optional)

Only include if relevant to your target roles.

```
- Title: {{TITLE}}
  Type: {{"project" | "publication" | "talk" | "open-source"}}
  Venue or URL: {{WHERE_IT_LIVES}}
  Year: {{YYYY}}
  One-line outcome: {{WHAT_IT_ACHIEVED_OR_COVERED}}
```

---

## 8. Gaps and Known Limitations

This section is for things you know are not in the file yet, or areas where you would need to go verify something before it can be used.

```
- {{e.g., "Accenture 2012-2014: need to confirm exact project names before using in bullets"}}
- {{e.g., "No documented metrics for OYO role; would need to ask former manager"}}
- {{e.g., "Career break 2019-2020: want to leave undocumented on resume"}}
```

When application-optimizer encounters a gap listed here, it will not try to fill it. It will either ask you or leave a placeholder in the output.

---

## 9. Off-Limits

Things you do not want included on any resume, even if they are true. Examples: a former employer you do not want to name, a qualification from a context you would rather not explain, a political or religious affiliation.

```
- {{OFF_LIMITS_ITEM_1}}
- {{OFF_LIMITS_ITEM_2}}
```

---

## Usage Notes

- **When you first run application-optimizer**, point it at this file. It will treat these entries as the authoritative source.
- **Keep this file plain markdown.** Do not use tables, images, or complex formatting; the skill needs to parse it reliably.
- **Re-read the file occasionally.** Your career keeps moving; this file should keep up.
- **Never delete metrics.** If a metric becomes stale, mark it with a date and move it to a "historical" section rather than removing it.

---

*Master Facts Template v1.0 | Career Helper Plugin | Prosper AI Consulting*
