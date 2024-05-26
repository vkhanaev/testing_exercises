import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test__compose_datetime_from__not_tomorrow():
    assert compose_datetime_from("not tomorrow", "23:59") ==\
           datetime.datetime.combine(datetime.datetime.now(), datetime.time(23, 59))


def test__compose_datetime_from__tomorrow():
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    assert compose_datetime_from("tomorrow", f"23:59") ==\
           datetime.datetime.combine(tomorrow, datetime.time(23, 59))


def test__compose_datetime_from__text_in_time():

    with pytest.raises(ValueError):
        compose_datetime_from("any text", f"not time")


def test__compose_datetime_from__not_valid_time():
    with pytest.raises(ValueError):
        compose_datetime_from("any text", f"41:99")
