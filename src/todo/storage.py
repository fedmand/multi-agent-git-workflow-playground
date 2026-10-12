"""Persistence of tasks in a JSON file. No printing, no argument parsing."""

from __future__ import annotations

from pathlib import Path

from todo.models import Task


def load_tasks(path: Path) -> list[Task]:
    """Return the tasks stored at `path`, in stored order.

    A missing or empty file means no tasks yet: return []. Corrupt JSON raises ValueError.
    """
    raise NotImplementedError


def save_tasks(path: Path, tasks: list[Task]) -> None:
    """Write `tasks` to `path` as JSON, creating parent folders if needed.

    Overwrites the previous contents. Output must be deterministic (stable key order).
    """
    raise NotImplementedError
