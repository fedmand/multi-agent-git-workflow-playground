"""Formatting of tasks for the terminal. Returns strings; never prints."""

from __future__ import annotations

from todo.models import Task


def format_task(task: Task) -> str:
    """One line per task, e.g. "[x] 3  Buy milk" (done) or "[ ] 3  Buy milk" (pending)."""
    box = "[x]" if task.done else "[ ]"
    return f"{box} {task.id}  {task.title}"


def format_task_list(tasks: list[Task]) -> str:
    """One format_task line per task, joined by newlines.

    An empty list returns "No tasks." (no trailing newline in either case).
    """
    if not tasks:
        return "No tasks."
    return "\n".join(format_task(t) for t in tasks)
