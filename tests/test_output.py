from __future__ import annotations

from todo.models import Task
from todo.output import format_task, format_task_list


def test_format_task_pending():
    assert format_task(Task(id=3, title="Buy milk")) == "[ ] 3  Buy milk"


def test_format_task_done():
    assert format_task(Task(id=3, title="Buy milk", done=True)) == "[x] 3  Buy milk"


def test_format_task_multi_digit_id():
    assert format_task(Task(id=123, title="Call mum")) == "[ ] 123  Call mum"


def test_format_task_list_several():
    tasks = [
        Task(id=1, title="One"),
        Task(id=2, title="Two", done=True),
        Task(id=10, title="Ten"),
    ]
    assert format_task_list(tasks) == "[ ] 1  One\n[x] 2  Two\n[ ] 10  Ten"


def test_format_task_list_single():
    assert format_task_list([Task(id=1, title="One")]) == "[ ] 1  One"


def test_format_task_list_empty():
    assert format_task_list([]) == "No tasks."


def test_no_trailing_newline():
    assert not format_task_list([]).endswith("\n")
    assert not format_task_list([Task(id=1, title="a"), Task(id=2, title="b")]).endswith("\n")
