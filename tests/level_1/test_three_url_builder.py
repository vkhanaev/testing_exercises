from functions.level_1.three_url_builder import build_url


def test_build_url():
    host = "host.ru"
    relative_url = "index.html"
    params = None
    expected_result = f"{host}/{relative_url}"
    assert build_url(host, relative_url, params) == expected_result

    params = {"a": "val_a"}
    expected_result = f"{host}/{relative_url}?{'&'.join(f'{k}={v}' for k, v in params.items())}"
    assert build_url(host, relative_url, params) == expected_result

    params = {"a": "val_a", "b": "val_b"}
    expected_result = f"{host}/{relative_url}?{'&'.join(f'{k}={v}' for k, v in params.items())}"
    assert build_url(host, relative_url, params) == expected_result

