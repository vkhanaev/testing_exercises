from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__correct_pull_request_url():
    assert is_github_pull_request_url("https://github.com/user/repo/pull/1") is True


def test__is_github_pull_request_url__len_splitted_url_is_not_7():
    assert is_github_pull_request_url("https://github.com/user/repo/pull/1/") is False


def test__is_github_pull_request_url__not_github_com():
    assert is_github_pull_request_url("https://any.host.ru/user/repo/pull/1") is False


def test__is_github_pull_request_url__not_pull():
    assert is_github_pull_request_url("https://github.com/user/repo/action/1") is False
