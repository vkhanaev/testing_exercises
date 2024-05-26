from functions.level_1.three_url_builder import build_url


def test__build_url__no_params():

    assert build_url("host.ru", "index.html") == "host.ru/index.html"


def test__build_url__one_parameter():
    assert build_url("host.ru", "index.html", get_params={"p": "value"}) == "host.ru/index.html?p=value"


def test__build_url__two_parameters():
    params = {"p1": "value1", "p2": "value2"}
    assert build_url("host.ru", "index.html", get_params=params) == "host.ru/index.html?p1=value1&p2=value2"

