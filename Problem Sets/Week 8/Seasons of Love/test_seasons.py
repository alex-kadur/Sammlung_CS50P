from seasons import check_date, get_age, convert_age


from datetime import date
import re
import sys
import inflect
import pytest


p = inflect.engine()


def test_check_date():
    assert check_date("2000-01-01") == date(2000, 1, 1)
    with pytest.raises(SystemExit):
        check_date("cat")
    with pytest.raises(SystemExit):
        check_date("2000-13-01")
    with pytest.raises(SystemExit):
        check_date("2000-01-32")


def test_get_age():
    assert get_age(date(2000, 1, 1)) == 8623


def test_convert_age():
    assert (
        convert_age(8623)
        == "twelve million, four hundred seventeen thousand, one hundred twenty"
    )
