from functions.level_1.five_title import change_copy_item


def test__change_copy_item__title_is_not_copy_and_not_enough_max_length():
    assert change_copy_item("Title", 1) == "Title"


def test__change_copy_item__title_is_not_copy_and_enough_max_length():
    assert change_copy_item("Title", 100) == "Copy of Title"


def test__change_copy_item__title_is_copy_and_not_enough_max_length():
    assert change_copy_item("Copy of Title", 1) == "Copy of Title"


def test__change_copy_item__title_is_copy_and_enough_max_length():
    assert change_copy_item("Copy of Title", 100) == "Copy of Title (2)"


def test__change_copy_item__title_is_copy_with_number_in_brackets_and_not_enough_max_length():
    assert change_copy_item("Copy of Title (1)", 1) == "Copy of Title (1)"


def test__change_copy_item__title_is_copy_with_number_in_brackets_and_enough_max_length():
    assert change_copy_item("Copy of Title (1)", 100) == "Copy of Title (2)"


def test__change_copy_item__title_is_copy_with_text_in_brackets_and_not_enough_max_length():
    assert change_copy_item("Copy of Title (text_with_digit_123)", 1) \
           == "Copy of Title (text_with_digit_123)"


def test__change_copy_item__title_is_copy_with_text_in_brackets_and_enough_max_length():
    assert change_copy_item("Copy of Title (text_with_digit_123)", 100) \
           == "Copy of Title (text_with_digit_123) (2)"
