import pytest

from functions.level_2.three_first import first, NOT_SET


def test__first__not_empty_items():
    assert first([9, 5, 2]) == 9


def test__first__empty_items_and_default_is_int():
    assert first([], 1) == 1


def test__first__empty_items_and_default_is_None():
    assert first([], None) is None


def test__first__empty_items_and_no_default():
    with pytest.raises(AttributeError):
        first([])


def test__first__empty_items_and_default_is_NOT_SET():
    with pytest.raises(AttributeError):
        first([], NOT_SET)


def test__first__empty_items_and_default_is_not_NOT_SET_str():
    assert first([], "not NOT_SET") == "not NOT_SET"
