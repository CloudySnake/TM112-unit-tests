def test_question_18(capsys):
    import src.block_quiz_01.question_18 as q18

    captured, err = capsys.readouterr()
    assert captured == "76 photos of 13 MB fit in 1000 MB\n"
