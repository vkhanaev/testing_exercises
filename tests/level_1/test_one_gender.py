import ast

from functions.level_1.one_gender import genderalize


def test__genderalize__gender_male():
    assert genderalize("M", "F", "male") == "M"


def test__genderalize__gender_notmale():
    assert genderalize("M", "F", "not male") == "F"
