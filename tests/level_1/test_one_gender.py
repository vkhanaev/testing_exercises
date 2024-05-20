from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("M", "F", "male") == "M"
    assert genderalize("M", "F", "not male") == "F"
