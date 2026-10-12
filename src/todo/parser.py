"""Turns command-line arguments into a Command. No I/O besides argparse's own errors."""

from __future__ import annotations

from todo.models import Command


def parse_args(argv: list[str]) -> Command:
    """Parse `argv` (without the program name) into a Command.

    Supported:
        add <title...>   -> Command("add", title="<title joined by spaces>")
        list             -> Command("list")
        done <id>        -> Command("done", task_id=<id>)
        rm <id>          -> Command("rm", task_id=<id>)

    Invalid input (unknown command, missing/non-integer id, empty title) raises
    SystemExit(2), which is argparse's default behaviour.
    """
    raise NotImplementedError
