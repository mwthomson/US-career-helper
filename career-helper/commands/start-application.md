---
description: Score a role's fit before you apply, then auto-run networking and resume prep on a strong fit
argument-hint: "[job description, URL, or role and company]"
---

# Career Helper - Start Application

You are helping the user decide whether a specific role is worth applying to, and
running the first steps of the application if it is.

## Accessibility Check

**Before starting**, check for `career-helper-preferences.md` in the current
working directory using the Glob tool. If found, read the YAML frontmatter and
apply accessibility preferences (dyslexia-friendly formatting, color-blind safe
output) for the remainder of this interaction.

If **no preferences file exists**, ask once: "Do you have any accessibility
preferences I should know about? For example, if you're dyslexic I can adjust how
I format things." If yes, save to `career-helper-preferences.md` using the format
documented in the Tim skill. If the user declines, proceed without creating the
file.

---

## Start

Invoke the **start-application** skill. If the user supplied a job description,
URL, or role and company as an argument, pass it straight through as the job
description input for Stage 1. If they supplied nothing, ask for the job
description or its URL before starting Stage 1.
