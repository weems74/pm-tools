# pm-tools

Collection of AI-powered tools for product management workflows.

## Agents

| Agent | Purpose |
|---|---|
| **Ecosystem & Competition** | Gather, prioritise, and summarise your product's ecosystem and competitive landscape |
| **Idea** | Flesh out, structure, and stress-test ideas for new projects or features |
| **Day Planner** | Prioritise tasks, protect focus time, and build a realistic daily plan |

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key

```bash
export OPENAI_API_KEY="sk-..."
```

## Usage

### Interactive menu (recommended)

```bash
python main.py
```

You'll see a numbered menu — pick an agent and start chatting.  
Type `/reset` to clear the conversation, `/quit` to exit.

### Launch an agent directly

```bash
python main.py --agent ecosystem   # competitive intelligence
python main.py --agent idea        # ideation & feature scoping
python main.py --agent planner     # daily prioritisation
```

### Use a different model

```bash
python main.py --model gpt-4o-mini   # faster / cheaper
```

## Project structure

```
pm-tools/
├── main.py                     # CLI entry point
├── requirements.txt
└── agents/
    ├── __init__.py
    ├── base_agent.py           # shared base class
    ├── ecosystem_agent.py      # ecosystem & competition research
    ├── idea_agent.py           # ideation & feature scoping
    └── day_planner_agent.py    # daily prioritisation & planning
```
