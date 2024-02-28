# three or more functions that collectively test implementation of count

import pytest
from um import count


def test_count_1():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("Um, hello, UM, world") == 2
    assert count("um, hello, UM, world") == 2


def test_count_2():
    assert count("yummy") == 0
    assert count("tummy") == 0
    assert count("um, umm, ummm") == 1
    assert count("umumum, um") == 1


def test_count_3():
    assert count("cat") == 0
    assert count("123") == 0
    assert count("") == 0
