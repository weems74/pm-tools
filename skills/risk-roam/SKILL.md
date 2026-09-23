---
name: risk-roam
description: "Run a structured Q&A risk review for an idea, product, feature, workflow, or system. Use when the user wants to think through risks, edge cases, failure modes, integrations, scalability, interoperability, accessibility, localization, security, privacy, legal or data-use concerns, or apply the ROAM framework."
---

# Risk ROAM

Run a focused, conversational risk-discovery session. The goal is not to produce an exhaustive checklist; it is to expose decision-relevant risks, test assumptions with questions, and leave each meaningful risk with a clear disposition.

ROAM means:

- **Resolve**: evidence or a decision removes the risk.
- **Own**: a named person or team must investigate or manage it.
- **Accept**: the risk is understood and consciously accepted for now.
- **Mitigate**: a concrete control, design change, experiment, or fallback reduces likelihood or impact.

Do not treat an unexamined risk as Accepted. Acceptance requires an explicit rationale and an appropriate decision-maker.

## Session contract

At the beginning:

1. Restate the idea and the decision or next step the review should support.
2. Ask for missing context one or two questions at a time: intended users, lifecycle stage, geography, data, dependencies, and constraints.
3. Explain that the review will be adaptive. Start with the risk areas most likely to change the decision, then expand based on what is discovered.

During the session:

- Ask one or two targeted questions at a time. Prefer questions that could change the design or go/no-go decision.
- Separate facts, assumptions, unknowns, and recommendations.
- Use concrete failure scenarios: trigger, failure, affected party, impact, detection, and recovery.
- Do not invent regulatory requirements, vendor capabilities, user behaviour, or legal conclusions. Mark them as unknowns and recommend validation.
- Treat legal, privacy, security, accessibility, and data-use concerns as areas for qualified review, not as definitive legal or compliance advice.
- Avoid repeating a category once it has been adequately covered unless new evidence changes the risk.
- When a new class of failure appears, capture it as a candidate extension to the catalogue.

At useful checkpoints, summarize:

- What is now known.
- The highest-impact unresolved risks.
- Which risks can be resolved by clarification or evidence.
- Which risks need an owner, mitigation, acceptance decision, or escalation.

## Risk discovery lenses

Use these lenses as a starting catalogue, selecting the relevant ones rather than reciting all of them:

1. **Obscure error states and edge cases**: invalid, missing, stale, duplicated, partial, malformed, concurrent, reordered, or unexpectedly large inputs; retries, timeouts, cancellations, recovery, and degraded modes.
2. **Business logic**: conflicting rules, ambiguous states, permissions, calculations, lifecycle transitions, defaults, reversals, idempotency, and unmet operational rules.
3. **Domain knowledge**: incorrect assumptions, missing terminology, expert workflows, safety considerations, and cases where the team cannot reliably judge correctness.
4. **Integrations and ecosystem**: authentication, versioning, rate limits, webhooks, retries, ownership boundaries, vendor outages, incompatible assumptions, and how neighbouring systems react.
5. **Data interoperability**: identifiers, schemas, units, encoding, time zones, precision, provenance, consent, retention, deletion, migration, synchronization, and conflict resolution.
6. **Scalability and operability**: volume, latency, concurrency, cost, quotas, hotspots, queue backlogs, observability, support load, deployment, rollback, and regional failure.
7. **Localization and translation**: language, locale, dates, numbers, currency, pluralization, text expansion, right-to-left layout, cultural meaning, and region-specific policy or availability.
8. **Accessibility and inclusive use**: keyboard and screen-reader flows, focus, semantics, contrast, motion, timing, error recovery, assistive technology, cognitive load, and alternative input.
9. **Security**: authentication, authorization, tenant isolation, secrets, injection, abuse, supply chain, logging, monitoring, incident response, and least privilege.
10. **Privacy**: collection, purpose limitation, notice, consent or other lawful basis, sensitive data, access, correction, deletion, retention, sharing, profiling, and breach impact.
11. **Legal and policy**: intellectual property, contracts, consumer protection, regulated decisions, terms of service, licensing, records, jurisdiction, and required review.
12. **Data provenance and terms of use**: where data came from, who collected it, what the source terms permit, whether the intended use is compatible, onward sharing, model or analytics use, and whether consent or permission covers it.

The catalogue is deliberately extensible. Add a lens when a new recurring risk class is found; do not force every future risk into an existing label.

## Q&A method

For each promising risk, ask questions in this order as needed:

1. **Scenario**: What could happen, and under what conditions?
2. **Impact**: Who or what is affected, and how severe is it?
3. **Likelihood and evidence**: What makes this plausible? What would disconfirm it?
4. **Detection**: How would we know it happened or is about to happen?
5. **Response**: Can we prevent, contain, recover, or communicate it?
6. **Decision**: Should we Resolve, Own, Accept, or Mitigate it?
7. **Accountability**: Who takes the next action, by when, and what evidence closes it?

Do not ask every question mechanically. Stop when the risk has a defensible disposition and next step.

## ROAM decision rules

- **Resolve** only when the concern is removed by evidence, a clarified requirement, a constrained scope, or a decision that makes the scenario impossible or irrelevant.
- **Own** when the concern remains open and a person or team can investigate or manage it. Record an owner, next action, due point, and escalation path.
- **Accept** only when the residual risk is understood, its impact is tolerable, and an accountable decision-maker accepts it. Record the rationale and review trigger.
- **Mitigate** when a planned control or change reduces likelihood or impact. Record the mitigation, residual risk, verification method, and owner.

Escalate risks when they cross team, product, organizational, geographic, or regulatory boundaries, or when the session cannot establish an accountable owner.

## Output

End with a concise review record containing:

### Context and assumptions
- Idea or system:
- Intended users:
- Decision being supported:
- Key assumptions:

### ROAM board
| Risk | Category | Trigger / failure scenario | Impact | Likelihood | Evidence / confidence | ROAM status | Owner or mitigation | Follow-up / due point |
|---|---|---|---|---|---|---|---|---|

### Decision summary
- Go / pause / change direction:
- Top unresolved risks:
- Assumptions requiring validation:
- Escalations:
- Next review trigger:

### Catalogue extensions
Record any new recurring category or prompt that should be added to this skill, with the example that exposed it and the reason the existing lenses were insufficient.

If the user asks for a shorter output, preserve at minimum: the risk, impact, ROAM status, owner or mitigation, and next action.

## Extension protocol

When a session reveals a recurring risk that the catalogue misses:

1. Name the new risk lens in plain language.
2. Give one concrete example that exposed it.
3. Explain why an existing lens was insufficient.
4. Add three to five prompts that distinguish this lens from nearby categories.
5. Add the lens to `Risk discovery lenses` only after it has recurred or materially changed a decision.
6. Keep the catalogue organized by the kind of failure or decision it helps uncover, not by a particular technology or vendor.

The skill itself should remain a reusable review workflow. Domain-specific checklists belong in separate assets or companion skills so the core process can evolve without becoming a giant static questionnaire.
