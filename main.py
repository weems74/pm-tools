#!/usr/bin/env python3
"""PM-Tools — main entry point.

Run this script to launch an interactive agent session:

    python main.py

You can also skip the menu and launch an agent directly:

    python main.py --agent ecosystem
    python main.py --agent idea
    python main.py --agent planner
"""

from __future__ import annotations

import argparse
import sys

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from agents import DayPlannerAgent, EcosystemAgent, IdeaAgent
from agents.base_agent import BaseAgent

console = Console()

AGENTS: dict[str, BaseAgent] = {
    "ecosystem": EcosystemAgent(),
    "idea": IdeaAgent(),
    "planner": DayPlannerAgent(),
}


def print_menu() -> None:
    table = Table(show_header=True, header_style="bold cyan", box=None)
    table.add_column("#", style="bold", width=3)
    table.add_column("Agent", style="bold cyan")
    table.add_column("What it does")

    for i, (key, agent) in enumerate(AGENTS.items(), start=1):
        table.add_row(str(i), agent.name, agent.description)

    console.print(
        Panel(
            table,
            title="[bold]PM-Tools[/bold]",
            subtitle="[dim]Your product management assistant[/dim]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def pick_agent() -> BaseAgent:
    """Interactively ask the user which agent to launch."""
    print_menu()
    keys = list(AGENTS.keys())
    while True:
        choice = Prompt.ask(
            "\nEnter agent number or name",
            default="1",
        ).strip().lower()

        # Accept numeric choice
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(keys):
                return AGENTS[keys[idx]]
            console.print(f"[red]Please enter a number between 1 and {len(keys)}.[/red]")
            continue

        # Accept key name or partial match
        if choice in AGENTS:
            return AGENTS[choice]

        matches = [k for k in keys if k.startswith(choice)]
        if len(matches) == 1:
            return AGENTS[matches[0]]

        console.print(
            f"[red]Unknown agent '{choice}'. "
            f"Valid names: {', '.join(keys)}[/red]"
        )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="pm-tools",
        description="PM-Tools: AI agents for your product management workflow.",
    )
    parser.add_argument(
        "--agent",
        choices=list(AGENTS.keys()),
        help="Launch a specific agent directly (skips the menu).",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o",
        help="OpenAI model to use (default: gpt-4o).",
    )
    args = parser.parse_args(argv)

    # Apply model override to all agents
    if args.model != "gpt-4o":
        for agent in AGENTS.values():
            agent.model = args.model

    if args.agent:
        agent = AGENTS[args.agent]
    else:
        try:
            agent = pick_agent()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Goodbye![/dim]")
            sys.exit(0)

    console.print()
    agent.run()


if __name__ == "__main__":
    main()
