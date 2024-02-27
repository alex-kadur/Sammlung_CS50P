import pytest
from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("123/1000") == 12
    assert convert("128/1000") == 13
    with pytest.raises(ValueError):
        convert("A")
    with pytest.raises(ValueError):
        convert("2")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(70) == "70%"
