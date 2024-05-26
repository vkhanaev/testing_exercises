from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__zero_good_words_count_and_zero_bad_words_count():
    assert check_tweet_sentiment("word", {"good"}, {"bad"}) is None


def test__check_tweet_sentiment__good_words_count_equal_bad_words_count():
    assert check_tweet_sentiment("good bad", {"good"}, {"bad"}) is None


def test__check_tweet_sentiment__good_words_count_more_bad_words_count():
    assert check_tweet_sentiment("good", {"good"}, {"bad"}) == 'GOOD'


def test__check_tweet_sentiment__good_words_count_less_bad_words_count():
    assert check_tweet_sentiment("bad", {"good"}, {"bad"}) == 'BAD'


def test__check_tweet_sentiment__good_words_count_more_bad_words_count_and_words_is_capital():
    assert check_tweet_sentiment("GOOD", {"good"}, {"bad"}) == 'GOOD'
