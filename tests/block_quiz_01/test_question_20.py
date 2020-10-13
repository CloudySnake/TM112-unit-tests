"""
In order for this to work you will need to comment out the line in the question code
magnitude = get_input()

and replace with

magnitude = input()
"""
import importlib
from pytest import mark


test_cases = [
    (1, "That is a minor earthquake.\n"),
    (3.9, "That is a minor earthquake.\n"),
    (4, "That is a moderate earthquake.\n"),
    (5.9, "That is a moderate earthquake.\n"),
    (6, "That is a strong earthquake.\n"),
    (6.9, "That is a strong earthquake.\n"),
    (7, "That is a major earthquake.\n"),
    (7.9, "That is a major earthquake.\n"),
    (8, "That is a great earthquake.\n"),
    (9.5, "That is a great earthquake.\n"),
]


@mark.parametrize("test_input, expected_output", test_cases)
def test_question_20(mocker, capsys, test_input, expected_output):
    mocker.patch("builtins.input", return_value=test_input)
    import src.block_quiz_01.question_20 as q20

    capsys.readouterr()
    importlib.reload(q20)
    captured = capsys.readouterr()
    assert captured.out == expected_output
