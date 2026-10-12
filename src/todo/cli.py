"""Glue: parse args, apply the command to the stored tasks, print the result.

Implemented after storage, parser and output are merged.
"""

from __future__ import annotations

from pathlib import Path

DEFAULT_PATH = Path.home() / ".todo.json"


def main(argv: list[str] | None = None, path: Path = DEFAULT_PATH) -> int:
    """Run the CLI; return the process exit code (0 on success)."""
    raise NotImplementedError
