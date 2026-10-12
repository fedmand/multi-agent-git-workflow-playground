import pytest

from todo.models import Task
from todo.storage import load_tasks, save_tasks


def test_round_trip_preserves_order(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [Task(2, "b", True), Task(1, "a"), Task(3, "ñ ü")]
    save_tasks(path, tasks)
    assert load_tasks(path) == tasks


def test_round_trip_empty_list(tmp_path):
    path = tmp_path / "tasks.json"
    save_tasks(path, [])
    assert load_tasks(path) == []


def test_missing_file_returns_empty(tmp_path):
    assert load_tasks(tmp_path / "nope.json") == []


def test_empty_file_returns_empty(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("", encoding="utf-8")
    assert load_tasks(path) == []


def test_corrupt_json_raises_value_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(ValueError):
        load_tasks(path)


def test_wrong_shape_raises_value_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"id": 1}', encoding="utf-8")
    with pytest.raises(ValueError):
        load_tasks(path)
    path.write_text('[{"id": 1}]', encoding="utf-8")
    with pytest.raises(ValueError):
        load_tasks(path)


def test_save_creates_parent_folders(tmp_path):
    path = tmp_path / "a" / "b" / "tasks.json"
    save_tasks(path, [Task(1, "x")])
    assert load_tasks(path) == [Task(1, "x")]


def test_save_overwrites(tmp_path):
    path = tmp_path / "tasks.json"
    save_tasks(path, [Task(1, "x"), Task(2, "y")])
    save_tasks(path, [Task(3, "z")])
    assert load_tasks(path) == [Task(3, "z")]


def test_output_is_deterministic(tmp_path):
    p1 = tmp_path / "one.json"
    p2 = tmp_path / "two.json"
    tasks = [Task(1, "a", True), Task(2, "b")]
    save_tasks(p1, tasks)
    save_tasks(p2, tasks)
    save_tasks(p2, tasks)
    assert p1.read_bytes() == p2.read_bytes()
    assert p1.read_text(encoding="utf-8").index('"done"') < p1.read_text(
        encoding="utf-8"
    ).index('"id"')
