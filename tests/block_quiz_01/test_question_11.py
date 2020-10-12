import importlib
from pytest import mark


test_cases = [
    ("1, 2, 3", 4),
    ("1, 2, 3, 4, 5", 6),
    ("10, 2, 3, 4, 5", 15),
    ("1, 2, 3, 4, -5", -4),
    ("2, 3, 4, 5", 7),
    ("10, 11, 12, 13, 14", 24),
    ("10, 11, 12, 13, 14, 15", 25),
]


@mark.parametrize("test_input, expected_output", test_cases)
def test_question_11(mocker, test_input, expected_output):
    """
    This feels super hacky having to use importlib, but it does work
    """
    mocker.patch("builtins.input", return_value=test_input)
    import src.block_quiz_01.question_11 as q11

    importlib.reload(q11)
    assert q11.first_plus_last == expected_output
