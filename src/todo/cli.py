"""Glue: parse args, apply the command to the stored tasks, print the result."""

from __future__ import annotations

import sys
from pathlib import Path

from todo.models import Task
from todo.output import format_task, format_task_list
from todo.parser import parse_args
from todo.storage import load_tasks, save_tasks

DEFAULT_PATH = Path.home() / ".todo.json"


def main(argv: list[str] | None = None, path: Path = DEFAULT_PATH) -> int:
    """Run the CLI; return the process exit code (0 on success)."""
    try:
        cmd = parse_args(sys.argv[1:] if argv is None else argv)
    except SystemExit as exc:
        return int(exc.code or 0)

    tasks = load_tasks(path)

    if cmd.name == "list":
        print(format_task_list(tasks))
        return 0

    if cmd.name == "add":
        task = Task(id=max((t.id for t in tasks), default=0) + 1, title=cmd.title or "")
        tasks.append(task)
        save_tasks(path, tasks)
        print(format_task(task))
        return 0

    target = next((t for t in tasks if t.id == cmd.task_id), None)
    if target is None:
        print(f"No task with id {cmd.task_id}.", file=sys.stderr)
        return 1

    if cmd.name == "done":
        target.done = True
        print(format_task(target))
    else:  # "rm"
        tasks.remove(target)
        print(f"Removed {target.id}.")
    save_tasks(path, tasks)
    return 0
