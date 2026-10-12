"""Turns command-line arguments into a Command. No I/O besides argparse's own errors."""

from __future__ import annotations

import argparse

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
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("title", nargs="+", help="task title")
    sub.add_parser("list", help="list tasks")
    done = sub.add_parser("done", help="mark a task as done")
    done.add_argument("task_id", type=int, help="task id")
    rm = sub.add_parser("rm", help="remove a task")
    rm.add_argument("task_id", type=int, help="task id")

    args = parser.parse_args(argv)
    if args.command == "add":
        title = " ".join(args.title).strip()
        if not title:
            add.error("title must not be empty")
        return Command("add", title=title)
    if args.command == "list":
        return Command("list")
    return Command(args.command, task_id=args.task_id)
