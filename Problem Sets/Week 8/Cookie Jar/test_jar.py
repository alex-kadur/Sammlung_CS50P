from jar import Jar
import pytest

# info:
# mock (i.e., simulate) state when testing methods
# Python’s own mock object library
# call just the one method but modify the underlying state first, without calling the other method to do so


# assert that this jar has the capacity it should
def test_init():
    jar = Jar()
    jar.capacity = 12
    jar = Jar(5)
    jar.capacity = 5


# assert that str(jar) prints out as many cookies as have been deposited
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


# assert that the jar’s size attribute is as large as the number of cookies that have been deposited
# assert that, if you deposit more than the jar’s capacity, deposit should raise a ValueError
def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(12)


# assert that withdrawing from the jar leaves the appropriate number of cookies in the jar’s size attribute
# assert that, if you withdraw more than the jar’s size, withdraw should raise a ValueError
def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(8)
