---
name: ticket-refiner
description: Turn rough notes, meeting bullets, Slack fragments, or half-formed requests into a clear, reviewable markdown ticket with background, acceptance criteria, dependencies, risks, and open questions. Use this whenever the user wants to write, draft, clean up, refine, or "ticketize" a story, bug, task, or feature request — even if they just paste messy notes and say "make this a ticket" or "can engineering work from this?"
---

# Ticket Refiner

Turn messy input into a ticket draft a team can edit, challenge, and hand to engineering. The goal is not to sound clever; it is to make the real work and the real unknowns visible.

## Workflow

1. **Gather context before drafting.** If the repo has product or team context, use it:
   - `context/ticket-conventions.md` (label taxonomy, definition of done, sign-off rules), if present
   - Existing tickets in `tickets/` or similar, to match tone and structure
   - Linked or mentioned docs (PRDs, research notes) the user references

   Repo conventions override the defaults in this skill.

2. **Clarify only when needed.** If a critical detail is missing, ask up to three focused questions before drafting. Prioritize, in order: scope, user impact, constraints, hard deadlines or dependencies. If the gaps are minor, draft anyway and put them in **Open questions**.

3. **Refine the signal.** Separate the actual problem from noisy wording, solution bias ("just add a button"), and background chatter. When the source material is fuzzy, say what you assumed.

4. **Draft the ticket** using `assets/ticket-template.md`. Save it as a markdown file if the user is working in a repo; otherwise return it inline.

## Sections

Required, always present:
- **Title** — specific and action-oriented ("Add CSV export to monthly claims report", not "Export improvements")
- **Background** — the problem, relevant context, and desired outcome, in one concise section
- **Acceptance criteria** — a short checklist
- **Dependencies / stakeholders**
- **Risks / unknowns** — keep minimal or leave blank if none are evident; never invent risks
- **Open questions**

Optional, include only when they earn their place:
- **Scope** — only to narrow broad work, clarify ownership boundaries, or name meaningful out-of-scope items
- **Resources** — only when there are real links or references in the source material
- **Labels** — only when provided or obvious from the source material

## Acceptance criteria defaults

Unless repo conventions say otherwise:
- Always include updating unit / integration / system tests.
- Usually include basic validation of the change.
- Always include review sign-off from the product lead.

## Drafting rules

- Distinguish facts from assumptions. Mark assumptions inline, e.g. *(assumed — confirm)*.
- If notes are incomplete, still produce the best draft possible and list what needs confirmation under **Open questions**.
- Preserve cross-team coordination items. When another team, stakeholder, or external dependency is involved, capture it in **Dependencies / stakeholders**, **Acceptance criteria**, or **Open questions** as appropriate.
- Be concise and concrete. No filler, hype, or generic PM language.

## After drafting

End with one or two lines naming the biggest gap or assumption the PM should resolve before refinement. Don't summarize the ticket back to them.
