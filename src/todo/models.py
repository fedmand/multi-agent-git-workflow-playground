"""Shared data types. Every other module depends on these; keep them minimal."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


@dataclass
class Command:
    """A parsed CLI invocation.

    name: one of "add", "list", "done", "rm".
    title: text for "add", otherwise None.
    task_id: target id for "done" and "rm", otherwise None.
    """

    name: str
    title: str | None = None
    task_id: int | None = None
