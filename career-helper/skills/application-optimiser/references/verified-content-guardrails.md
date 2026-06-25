# Verified Content Guardrails

**Purpose:** Prevent hallucination, fabrication, and unverifiable embellishment when rewriting or optimising a user's resume. Every word in a delivered resume must trace to a source the user has provided or confirmed.

**Applies to:** All resume and bullet-level output produced by application-optimiser. Research briefs and interview prep have their own citation rules (see `deep-research-reflection.md`).

---

## The Iron Rule

**Never invent, extrapolate, or infer details about work history, achievements, metrics, scope, or background.** If a detail is not in the user's source material (their current resume, a master facts file, or explicit clarification in the conversation), do not write it.

When a bullet would benefit from a detail you cannot verify, flag it and ask. Never fill the gap yourself.

This rule is non-negotiable. A shorter bullet with verified content is always preferable to a longer bullet with inferred content.

---

## Sources of Truth, in Priority Order

1. **Master facts file** (if present in cwd), typically `master-facts.md` or similar. Pre-verified timeline, metrics, and bullet library. When present, treat as authoritative.
2. **The user's current resume.** Verified content by default; ask only if something looks inconsistent or dated.
3. **Explicit conversation turns.** Facts the user has confirmed in chat.
4. **Job description.** Source for target keywords only, never for candidate history.

Never pull candidate content from a sample or template resume. Templates are for layout only.

---

## Trigger Phrases: If You Find Yourself Writing These, Stop

These phrases usually signal that you are about to invent or infer. When one appears in your draft, check whether every substantive word traces to a verified source before continuing.

- "Based on your experience...": is the experience you are about to describe actually documented?
- "Given your background...": verified or assumed?
- "You also...": is this in the source material?
- "Your cross-functional...": was "cross-functional" in the source, or are you adding it?
- "Your award-winning...": verified award, or editorialising?
- "Your innovative...": verified, or marketing language?
- "Strategic leader with...": generic positioning you are inventing?

If you catch yourself mid-sentence using one of these, stop and check the source.

---

## Decision Tree: Is This Content Safe to Include?

Before including any substantive word, phrase, or claim in a delivered bullet:

1. **Can you cite the source?** (Master facts section, resume section, or a specific conversation turn.)
   - No: do not include. Flag for clarification.
   - Yes: continue.

2. **Are you using the exact words from the source?**
   - Yes: safe to include.
   - No: continue.

3. **Have you only removed redundant words, without changing meaning?**
   - Yes: safe to include.
   - No: continue.

4. **Are you choosing between two verified alternatives in the source?**
   - Yes: safe to include. Document the choice in your internal reasoning.
   - No: flag for user clarification.

If the decision tree ever exits at "flag for clarification", the default action is to ask the user, not to guess.

---

## Safe Optimisation: What You Are Allowed to Do

These operations preserve meaning while improving readability:

- Remove redundant connectors: "in order to" becomes "to".
- Consolidate structure: "that included X, Y, and Z" becomes "via X, Y, and Z".
- Use a participial phrase in place of a relative clause: "that reached" becomes "reaching".
- Choose between two verified phrasings in the source (e.g., the library has both "led" and "co-led"; pick the one the source actually uses for that specific achievement).
- Choose the more specific of two verified alternatives when both are in the source (e.g., use the specific platform name rather than the generic platform type if both are in the source).
- Reorder elements within a bullet as long as no meaning shifts.
- Apply US English spelling.

---

## Unsafe Changes: Never Do These

These operations introduce unverifiable content:

- **Adding emphasis modifiers not in the source.** Never add "strategic", "innovative", "comprehensive", "robust", "high-performing", "world-class" if they are not already in the source.
- **Specifying team composition not in the source.** Never add "cross-functional", "distributed", "diverse", "matrixed" unless explicitly documented.
- **Adding geographic scope not in the source.** Never add "across X countries" or "in region Y" without verification, even if the company operates there.
- **Inferring reporting structure.** Never add "direct reports", "dotted line", "matrixed" unless documented.
- **Adding timing details not verified.** Never add "within six months", "in the first quarter", "by year-end" unless the source says so.
- **Combining metrics from different bullets.** If the source has two separate achievements, do not merge them into one bullet.
- **Creating hybrid bullets.** Do not combine elements from different source bullets into a new bullet that was never verified as a single statement.
- **Changing attribution.** Never change "led" to "co-led" (or vice versa) without explicit verification.
- **Inferring scope or scale.** If the source says "team", do not write "team of twelve" unless the number is documented.

---

## Examples: Safe and Unsafe

### Example 1: Removing layoff (safe)

**Source bullet:** "Built and scaled a team that reached 2.5 million monthly active users through email, paid social, and organic search."

**Safe rewrite:** "Built and scaled a team reaching 2.5 million monthly active users via email, paid social, and organic search."

What changed: "that reached" became "reaching", "through" became "via". All metrics and channels preserved exactly.

### Example 2: Adding unverified emphasis (unsafe)

**Source bullet:** "Built and scaled a team that reached 2.5 million monthly active users through email, paid social, and organic search."

**Unsafe rewrite:** "Built and scaled a high-performing, cross-functional team that strategically engaged 2.5 million monthly active users through integrated email, paid social, and organic search channels."

What went wrong: "high-performing", "cross-functional", "strategically engaged", and "integrated...channels" were all added. None of those modifiers was in the source. "Reached" was changed to "strategically engaged", which adds intent the source does not document.

### Example 3: Choosing between verified alternatives (safe)

**Source has two versions of the same achievement:**
- A: "Managed a twelve-person product team across London, Berlin, and Singapore."
- B: "Built and scaled a twelve-person product team."

**Safe:** Use A when the target role emphasises global scale. Use B when the target role emphasises team building. Both are verified.

**Unsafe:** Combining into "Built and scaled a twelve-person product team across London, Berlin, and Singapore." This combined phrasing was never verified as a single statement and risks misrepresenting whether the candidate built the team before or after the geographic expansion.

### Example 4: Preserving specificity (safe)

**Source bullet:** "Directly managed a team of five that grew weekly newsletter subscribers from 40k to 180k via HubSpot, LinkedIn, and Reddit."

**Safe rewrite preserves:** the modifier "directly", the specific platform names (HubSpot, LinkedIn, Reddit), the frequency ("weekly"), and the specific starting and ending metrics.

**Unsafe rewrite loses specificity:** "Managed a team that grew newsletter subscribers via multiple digital channels." This drops "directly" (a real modifier in the source), replaces specific platform names with a generic phrase, loses the frequency, and loses both metrics.

---

## Hallucination Red Flags: Self-Review Before Delivery

After drafting a resume but before presenting it, scan for these red flags in your own output:

- Adjectives not in the source: "strategic", "innovative", "comprehensive", "robust", "world-class", "industry-leading"
- Team composition you cannot cite: "cross-functional", "distributed", "diverse"
- Geographic details you cannot cite: "across X countries", "global", "EMEA-wide"
- Reporting structure you cannot cite: "direct reports", "dotted line", "matrixed"
- Timing details you cannot cite: "within X months", "in the first Y", "by Q3"
- Metrics that seem too clean or round compared to the source
- Hybrid bullets that stitch parts of different source bullets together

If any red flag appears, either remove it or verify it with the user before delivering.

---

## When You Must Ask

Ask the user (do not guess) when:

- The job description emphasises a skill or area that is adjacent to but not explicitly in the source material
- A metric in the source is outdated and you are unsure whether a newer number exists
- The source mentions a programme or initiative by generic reference and a specific name would help the bullet land
- Two source bullets contradict each other
- You need to fill a gap the source does not cover

The phrasing should be specific: "I can see you led a team at X but the source doesn't specify size. Do you have a headcount?" not "Do you want me to add more detail?"

---

## Final Verification Before Delivery

Before presenting a resume, answer each of these for every substantive bullet:

1. Can I cite the exact source (file and section, or conversation turn) where this content came from?
2. Are all substantive words in the bullet present in that source, or traceable to a verified alternative?
3. If I rephrased for flow, does the meaning remain identical to the source?
4. Have I only removed redundant words, never added meaning?
5. If uncertain about any element, have I flagged it for clarification rather than guessing?

If any answer is "no" or "unsure", fix the bullet before delivering.

---

*Verified Content Guardrails v1.0 | Career Helper Plugin | Prosper AI Consulting*
