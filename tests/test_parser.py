import pytest

from todo.models import Command
from todo.parser import parse_args


def test_add_single_word():
    assert parse_args(["add", "milk"]) == Command("add", title="milk")


def test_add_multi_word_title():
    assert parse_args(["add", "buy", "some", "milk"]) == Command("add", title="buy some milk")


def test_add_quoted_title():
    assert parse_args(["add", "buy milk"]) == Command("add", title="buy milk")


def test_list():
    assert parse_args(["list"]) == Command("list")


def test_done():
    assert parse_args(["done", "3"]) == Command("done", task_id=3)


def test_rm():
    assert parse_args(["rm", "12"]) == Command("rm", task_id=12)


@pytest.mark.parametrize(
    "argv",
    [
        [],
        ["bogus"],
        ["add"],
        ["add", ""],
        ["add", "  ", " "],
        ["done"],
        ["rm"],
        ["done", "abc"],
        ["rm", "1.5"],
        ["done", "x", "y"],
    ],
)
def test_invalid_input_exits_with_2(argv):
    with pytest.raises(SystemExit) as exc:
        parse_args(argv)
    assert exc.value.code == 2
