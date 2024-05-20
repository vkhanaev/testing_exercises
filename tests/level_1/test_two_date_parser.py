import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    now = datetime.datetime.now()
    test_date, test_time = now.strftime("%d.%m.%Y %H:%M").split()
    expected_result = datetime.datetime.strptime(f"{test_date} {test_time}", "%d.%m.%Y %H:%M")
    assert compose_datetime_from("какой-то текст", test_time) == expected_result

    test_time = "13:00".split(":")
    h = int(test_time[0])
    m = int(test_time[1])
    tomorrow = now + datetime.timedelta(days=1)
    expected_result = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, h, m)
    assert compose_datetime_from("tomorrow", f"{h}:{m}") == expected_result

    with pytest.raises(ValueError):
        compose_datetime_from("какой-то текст", f"текст вместо времени")

    with pytest.raises(ValueError):
        compose_datetime_from("какой-то текст", f"41:99")
