from todo.cli import main


def run(tmp_path, capsys, *argv):
    code = main(list(argv), path=tmp_path / "tasks.json")
    captured = capsys.readouterr()
    return code, captured.out.strip(), captured.err.strip()


def test_list_when_empty(tmp_path, capsys):
    assert run(tmp_path, capsys, "list") == (0, "No tasks.", "")


def test_add_then_list(tmp_path, capsys):
    assert run(tmp_path, capsys, "add", "Buy", "milk") == (0, "[ ] 1  Buy milk", "")
    run(tmp_path, capsys, "add", "Call", "Ana")
    assert run(tmp_path, capsys, "list")[1] == "[ ] 1  Buy milk\n[ ] 2  Call Ana"


def test_done_marks_task(tmp_path, capsys):
    run(tmp_path, capsys, "add", "Buy milk")
    assert run(tmp_path, capsys, "done", "1") == (0, "[x] 1  Buy milk", "")
    assert run(tmp_path, capsys, "list")[1] == "[x] 1  Buy milk"


def test_rm_removes_task_and_ids_are_not_reused(tmp_path, capsys):
    run(tmp_path, capsys, "add", "a")
    run(tmp_path, capsys, "add", "b")
    assert run(tmp_path, capsys, "rm", "1") == (0, "Removed 1.", "")
    assert run(tmp_path, capsys, "list")[1] == "[ ] 2  b"
    assert run(tmp_path, capsys, "add", "c")[1] == "[ ] 3  c"


def test_unknown_id_fails(tmp_path, capsys):
    code, out, err = run(tmp_path, capsys, "done", "9")
    assert (code, out) == (1, "")
    assert "No task with id 9" in err


def test_invalid_args_return_exit_code_2(tmp_path, capsys):
    assert run(tmp_path, capsys, "bogus")[0] == 2
    assert run(tmp_path, capsys)[0] == 2
