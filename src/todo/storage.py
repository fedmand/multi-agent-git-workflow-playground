"""Persistence of tasks in a JSON file. No printing, no argument parsing."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from todo.models import Task


def load_tasks(path: Path) -> list[Task]:
    """Return the tasks stored at `path`, in stored order.

    A missing or empty file means no tasks yet: return []. Corrupt JSON raises ValueError.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    if not text.strip():
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"corrupt JSON in {path}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError(f"corrupt task file {path}: expected a JSON list")
    try:
        return [
            Task(id=item["id"], title=item["title"], done=item.get("done", False))
            for item in data
        ]
    except (TypeError, KeyError, AttributeError) as exc:
        raise ValueError(f"corrupt task entry in {path}: {exc!r}") from exc


def save_tasks(path: Path, tasks: list[Task]) -> None:
    """Write `tasks` to `path` as JSON, creating parent folders if needed.

    Overwrites the previous contents. Output must be deterministic (stable key order).
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps([asdict(t) for t in tasks], indent=2, sort_keys=True)
    path.write_text(text + "\n", encoding="utf-8")
