# Career Helper

A Claude Code plugin for end-to-end US career support: resume and cover letter
optimization, interview prep, LinkedIn coaching, job search strategy, career
transitions, personal branding, digital footprint review, and AI-governance
guidance for board directors (NEDs/governors/trustees).

It works for anyone job searching, at any career stage — graduate, mid-career,
senior/executive, returning after a break, navigating a layoff, or exploring a
career change.

## Requirements

- Claude Code (or another Claude surface that supports this plugin format:
  custom subagents, slash commands, and skills).
- No API keys or external accounts required. Some skills use web search for
  company/employer research.

## Install

Copy or clone this directory, then add it as a plugin the way you'd add any
local Claude Code plugin (see Claude Code's plugin documentation for the
current install command, since this can change between Claude Code versions).

## How to start

There are three ways in — pick whichever fits how you like to work:

1. **Guided coaching:** run `/career-helper:career-coach`. This launches Tim,
   an agent that asks a few questions about your situation, decides which
   skills you need and in what order, runs them for you, and checks in
   between each one. Best if you don't want to think about sequencing.

2. **Self-serve browsing:** run `/getting-started` (full walkthrough of
   everything the plugin can do, with examples) or `/career-helper:quick-start`
   (a shorter guided intake that routes you to the right skill). Best if you
   want to understand the whole toolkit before diving in, or want to stay in
   control of what runs when.

3. **Jump straight to a skill:** if you already know what you need, invoke it
   directly — see the table below.

Whichever path you take, run `/career-helper:status` any time to see your
progress and the outputs generated so far.

## Skills

| Skill | What it does | Best for |
|:------|:--------------|:---------|
| `/getting-started` | Full overview, preparation checklists, workflow planning, tips, scheduled Cowork routines | New users, or automating your search |
| `/linkedin-coach` | Profile audit, headlines, content strategy, post review, video scripts | Improving your LinkedIn presence |
| `/start-application` | Scored fit assessment before you apply: weighted rubric, gap interview, master-facts capture, and auto-handoff to networking and resume tailoring on a strong fit | Deciding whether a specific role is worth applying to |
| `/application-optimizer` | Company research, ATS resume rewriting, cover letters and supporting statements, application strategy | Applying for a specific role |
| `/interview-master` | Prep, mock interviews, post-interview coaching, reference and referee prep, ageism support | Before and after interviews |
| `/career-navigator` | Networking, 3-month plans, salary negotiation, offer evaluation, application tracker | Planning and tracking your search |
| `/career-transitions` | Portfolio/fractional careers, AI readiness, non-linear career exploration | Changing direction or exploring alternatives to traditional employment |
| `/employer-footprint` | Digital footprint audit through an employer's eyes, interview questions drawn from your online presence | Checking what employers will find about you online |
| `/social-media-review` | Quick social media check, privacy cleanup guide | Graduates, early career, or a fast health check |
| `/ned-ai-helper` | AI governance for boards, challenge frameworks, risk assessment | NEDs, governors, and trustees overseeing AI |
| `/ai-impact-assessment` | Assesses whether AI will materially disrupt your role in the next 12 months, with a mitigation plan | Checking if your role is at risk from AI |
| `/personal-brand` | Why You / Why Them / Why Now positioning, audience and channel map, bio library | Building or refreshing a personal brand, going fractional, positioning for board roles |
| `/career-helper:career-coach` | Tim: guided, adaptive coaching across all of the above | Anyone who wants guided support instead of picking skills themselves |

## Recommended sequencing

There's no single fixed order — Tim decides this dynamically based on your
situation, and `/getting-started`'s Workflow Planner will do the same if you
prefer to run skills yourself. As a rough starting point:

- **Actively applying to a specific role:** `/start-application` (fit check) →
  `/application-optimizer` → `/interview-master` → `/career-navigator` (offer
  evaluation/negotiation)
- **Starting a search from scratch:** `/getting-started` →
  `/employer-footprint` or `/social-media-review` → `/career-navigator`
  (3-month plan) → `/application-optimizer`
- **Considering a change in direction:** `/career-transitions` →
  `/personal-brand` → `/linkedin-coach`
- **Just had a layoff:** `/career-navigator` (career-returner support) →
  `/interview-master` (emotional support) → the active-search path above

## Privacy and accessibility

If you tell a skill about accessibility needs (e.g. dyslexia, color-blindness)
or share details about your situation, it can save them to
`career-helper-preferences.md` in your own working folder — always with your
consent first, never automatically. Nothing is sent anywhere else. You can ask
any skill or Tim to "forget me" at any time, which deletes the file.

## A note on accuracy

This plugin generates guidance with AI. It is not legal, tax, or financial
advice. Employment law, benefits, and tax treatment vary by state and change
over time — verify anything specific to your situation (deadlines, rights,
benefit eligibility) against an authoritative primary source (e.g. eeoc.gov,
your state's unemployment/workforce agency, or a licensed attorney) before
relying on it.

## A note on legal and benefits content

`/interview-master`'s ageism-related reference material and
`/career-navigator`'s career-returner reference material deliberately favor
short, accurate pointers to primary sources (eeoc.gov, your state's
unemployment/workforce agency, an employment attorney) over long, detailed
procedural tables. Employment law, benefit rules, and agency contact details
change and vary by state — a confidently detailed but stale or wrong summary
is worse than a short, correct pointer to where to check. Treat any specific
deadline, dollar figure, or organization name in this plugin as a starting
point for your own verification, not a final answer.

---
*Career Helper Plugin | Prosper AI Consulting*
