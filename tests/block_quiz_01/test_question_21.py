"""
In order for this to work you will need to comment out the line in the question code
seed = get_input()

and replace with

seed = input()
"""
import importlib
from pytest import mark

test_cases = [
    (3, "3\n0\n5\n2\n7\n4\n1\n6\n3\n"),
    (7, "7\n4\n1\n6\n3\n0\n5\n2\n7\n"),
]


@mark.parametrize("test_input, expected_output", test_cases)
def test_question_21(mocker, capsys, test_input, expected_output):
    mocker.patch("builtins.input", return_value=test_input)
    import src.block_quiz_01.question_21 as q21
    capsys.readouterr()
    importlib.reload(q21)
    captured = capsys.readouterr()
    assert captured.out == expected_output
