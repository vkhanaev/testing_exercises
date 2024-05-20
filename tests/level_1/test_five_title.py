from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    title = "Title"
    max_title_length = len(title) + len("Copy of ")
    expected_result = title
    assert change_copy_item(title, max_title_length) == expected_result

    max_title_length += 1
    expected_result = f"Copy of {title}"
    assert change_copy_item(title, max_title_length) == expected_result

    title = "Copy of Title"
    max_title_length = len(title) + len("Copy of ")
    expected_result = title
    assert change_copy_item(title, max_title_length) == expected_result

    max_title_length += 1
    expected_result = f"{title} (2)"
    assert change_copy_item(title, max_title_length) == expected_result

    title = "Copy of Title (1)"
    max_title_length = len(title) + len("Copy of ")
    expected_result = title
    assert change_copy_item(title, max_title_length) == expected_result

    max_title_length += 1
    words = title.split()
    last_word = words[-1]
    copy_cnt = int(last_word[1:-1])
    expected_result = f"{' '.join(words[:-1])} ({copy_cnt+1})"
    assert change_copy_item(title, max_title_length) == expected_result

    title = "Copy of Title (text_with_digit_123)"
    max_title_length = len(title) + len("Copy of ")
    expected_result = title
    assert change_copy_item(title, max_title_length) == expected_result

    max_title_length += 1
    expected_result = f"{title} (2)"
    assert change_copy_item(title, max_title_length) == expected_result
