from functions.level_2.five_replace_word import replace_word


def test__replace_word__one_word_replaced():
    assert replace_word("Some text to replace", "Replace", "check") == "Some text to check"


def test__replace_word__many_word_replaced():
    assert replace_word("Text to replace and replace and not replace!", "Replace", "check") == \
           "Text to check and check and not replace!"


def test__replace_word__nothing_replaced():
    assert replace_word("Some text to check", "Replace", "not replaced") == "Some text to check"
