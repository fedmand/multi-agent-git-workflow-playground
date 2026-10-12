from todo.models import Command, Task


def test_task_defaults_to_pending():
    assert Task(id=1, title="a").done is False


def test_command_optional_fields_default_to_none():
    cmd = Command("list")
    assert cmd.title is None and cmd.task_id is None
