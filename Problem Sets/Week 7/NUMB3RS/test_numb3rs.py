# implement 2+ functions that collectively test the implementation of validate in numb3rs.py
# each of whose names should begin with test_ so that you can execute your tests with pytest test_numb3rs.py

from numb3rs import validate


def test_validate_range():
    assert validate("255.255.255.255") == True
    assert validate("0.255.255.255") == True
    assert validate("255.0.255.255") == True
    assert validate("255.255.0.255") == True
    assert validate("255.255.255.0") == True
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
    assert validate("265.255.255.255") == False
    assert validate("255.265.255.255") == False
    assert validate("255.255.265.255") == False
    assert validate("255.255.255.265") == False
    assert validate("355.255.255.255") == False
    assert validate("255.355.255.255") == False
    assert validate("255.255.355.255") == False
    assert validate("255.255.255.355") == False


def test_validate_lenght():
    assert validate("255.255.255.255") == True
    assert validate("255.255.255") == False
    assert validate("255.255") == False
    assert validate("255") == False


def test_validate_char():
    assert validate("255.255.255.255") == True
    assert validate("255#255#255#255") == False
    assert validate("abc.255.255.255") == False
    assert validate("abc") == False


def test_validate_dot():
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.255.") == False
    assert validate(".255.255.255.255") == False
    assert validate("255..255..255..255") == False
