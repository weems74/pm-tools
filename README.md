# pm-tools

Agent skills for product management work: turning messy notes into reviewable tickets, and shaping raw ideas into stress-tested concepts.

Each skill is a folder with a `SKILL.md` file that follows the open [Agent Skills](https://agentskills.io) format, so the same files work in GitHub Copilot (CLI, VS Code agent mode), Claude Code, and other compatible agents.

## Skills

| Skill | What it does | Use it when |
|---|---|---|
| [`ticket-refiner`](skills/ticket-refiner/SKILL.md) | Turns rough notes, meeting bullets, or Slack fragments into a markdown ticket with background, acceptance criteria, dependencies, risks, and open questions | You have messy input and need something engineering can refine |
| [`idea-shaper`](skills/idea-shaper/SKILL.md) | Takes a raw idea through clarify → expand → structure → challenge, and saves a one-page concept | You have a half-formed idea and want to know if it holds up |
| [`risk-roam`](skills/risk-roam/SKILL.md) | Runs a structured Q&A risk review using the ROAM framework and captures decision-relevant risks with clear dispositions | You want to pressure-test an idea, product, feature, workflow, or system for risks before moving forward |

These skills separate facts from assumptions, surface gaps as open questions instead of inventing answers, and avoid filler.

## Install

Clone the repo, then link the skills into your personal skills folder so they're available in every project. Edits in this repo take effect immediately.

```bash
git clone https://github.com/weems74/pm-tools.git
mkdir -p ~/.copilot/skills

ln -s "$PWD/pm-tools/skills/ticket-refiner" ~/.copilot/skills/ticket-refiner
ln -s "$PWD/pm-tools/skills/idea-shaper"    ~/.copilot/skills/idea-shaper
ln -s "$PWD/pm-tools/skills/risk-roam"      ~/.copilot/skills/risk-roam
```

For Claude Code, link the same folders into `~/.claude/skills/` as well.

To use a skill in a single repository only, copy its folder into that repo's `.github/skills/` (or `.claude/skills/`) directory instead.

In Copilot CLI, run `/skills reload` after installing or editing a skill.

## Usage

No commands needed. The agent picks the skill based on what you ask:

- Paste meeting notes and say *"turn this into a ticket"* → `ticket-refiner`
- Say *"I have an idea for…"* or *"poke holes in this"* → `idea-shaper`

## Working with your own context

These skills look for context in the repository you're working in and use it when present:

```
your-repo/
├── context/
│   ├── ticket-conventions.md   # labels, definition of done, sign-off rules
│   └── product.md              # one-pager, users, strategy
├── tickets/                    # existing tickets, used to match your style
└── ideas/                      # concepts saved by idea-shaper
```

Repo conventions override the skills' defaults, so the output fits your team rather than a generic template.

## Repository structure

```
pm-tools/
└── skills/
    ├── ticket-refiner/
    │   ├── SKILL.md
    │   └── assets/ticket-template.md
    ├── idea-shaper/
    │   ├── SKILL.md
    │   └── assets/concept-template.md
    └── risk-roam/
        └── SKILL.md
```

## Evals

Each skill will include an `evals/` folder with realistic, sanitized input cases and written pass criteria, so changes to a skill can be checked against the same inputs over time. In progress.

## Background

This repo started as a Python CLI: four agents, each a system prompt wrapped in a chat loop calling the OpenAI API. After working with skill files directly in Copilot, it became clear the prompts were the real asset and the code was plumbing. A skill running inside an agent can read the repo it's working in, uses whichever model the host provides, and needs no API key or separate app.

The Python version is preserved in the commit history.

## License

<!-- Choose a license, e.g. MIT or Apache-2.0, and add a LICENSE file. -->
