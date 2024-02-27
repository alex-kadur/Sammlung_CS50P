from bank import value

def test_value():
    assert value("hello") == int(0)
    assert value("HELLO") == int(0)
    assert value("hell") == int(20)
    assert value("HELL") == int(20)
    assert value("CAT") == int(100)
    assert value("cat") == int(100)
    assert value("123") == int(100)
    assert value("...") == int(100)
    assert value("") == int(100)
  
