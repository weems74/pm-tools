"""Base agent class shared by all PM-Tools agents."""

from __future__ import annotations

import os
from abc import ABC, abstractmethod

from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


class BaseAgent(ABC):
    """Abstract base class for all PM-Tools agents.

    Subclasses must define:
    - ``name``         — display name shown in the UI
    - ``description``  — one-line description shown in the menu
    - ``system_prompt``— the OpenAI system prompt that shapes the agent's persona

    The ``run()`` method provides a ready-made interactive REPL that subclasses
    can use as-is or override.
    """

    # ------------------------------------------------------------------ #
    # Subclass interface                                                   #
    # ------------------------------------------------------------------ #

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name for this agent."""

    @property
    @abstractmethod
    def description(self) -> str:
        """One-line description shown in the agent selection menu."""

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """OpenAI system prompt that shapes the agent's behaviour."""

    # ------------------------------------------------------------------ #
    # Construction                                                         #
    # ------------------------------------------------------------------ #

    def __init__(self, model: str = "gpt-4o", api_key: str | None = None) -> None:
        self.model = model
        self._api_key = api_key
        self._client: OpenAI | None = None
        self._history: list[dict] = []
        self._reset_history()

    # ------------------------------------------------------------------ #
    # Public interface                                                     #
    # ------------------------------------------------------------------ #

    def run(self) -> None:
        """Start an interactive chat session with the agent."""
        console.print(
            Panel(
                f"[bold cyan]{self.name}[/bold cyan]\n[dim]{self.description}[/dim]",
                title="PM-Tools",
                border_style="cyan",
            )
        )
        console.print(
            "[dim]Type your message and press Enter. "
            "Commands: [bold]/reset[/bold] · [bold]/quit[/bold][/dim]\n"
        )

        while True:
            try:
                user_input = Prompt.ask("[bold green]You[/bold green]")
            except (EOFError, KeyboardInterrupt):
                console.print("\n[dim]Goodbye![/dim]")
                break

            if not user_input.strip():
                continue

            command = user_input.strip().lower()
            if command in ("/quit", "/exit", "/q"):
                console.print("[dim]Goodbye![/dim]")
                break
            if command == "/reset":
                self._reset_history()
                console.print("[dim]Conversation reset.[/dim]\n")
                continue

            reply = self._chat(user_input)
            console.print(f"\n[bold magenta]{self.name}[/bold magenta]")
            console.print(Markdown(reply))
            console.print()

    def chat(self, message: str) -> str:
        """Send a single message and return the assistant reply (non-interactive).

        Useful for scripted / programmatic use.
        """
        return self._chat(message)

    # ------------------------------------------------------------------ #
    # Internals                                                            #
    # ------------------------------------------------------------------ #

    def _reset_history(self) -> None:
        self._history = [{"role": "system", "content": self.system_prompt}]

    def _get_client(self) -> OpenAI:
        if self._client is None:
            self._client = OpenAI(
                api_key=self._api_key or os.environ.get("OPENAI_API_KEY")
            )
        return self._client

    def _chat(self, user_message: str) -> str:
        self._history.append({"role": "user", "content": user_message})
        response = self._get_client().chat.completions.create(
            model=self.model,
            messages=self._history,
        )
        reply = response.choices[0].message.content or ""
        self._history.append({"role": "assistant", "content": reply})
        return reply
