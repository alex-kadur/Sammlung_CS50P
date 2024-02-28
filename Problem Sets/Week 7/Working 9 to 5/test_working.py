import pytest
from working import convert


def test_convert_format_1():
    assert convert("1 AM to 3 PM") == "01:00 to 15:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_convert_format_2():
    assert convert("1:00 AM to 3:00 PM") == "01:00 to 15:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_convert_other():
    with pytest.raises(ValueError):
        convert("Cat")
    with pytest.raises(ValueError):
        convert("25 AM to 2 PM")
    with pytest.raises(ValueError):
        convert("1:60 AM to 2:15 PM")
