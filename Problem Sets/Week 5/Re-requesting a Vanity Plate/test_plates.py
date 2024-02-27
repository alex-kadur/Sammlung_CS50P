from plates import is_valid

#2 to 6 characters
#must start with 2 letters
#numbers must come at end eg. AAA222
#first number can't be 0
#no periods, spaces or punctuation
def test_is_valid():
    assert is_valid("AA") == True
    assert is_valid("AA1") == True
    assert is_valid("AAA1") == True
    assert is_valid("AAA11") == True
    assert is_valid("AAA10") == True
    assert is_valid("AAA111") == True
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("A1") == False
    assert is_valid("AAA01") == False
    assert is_valid("AAAA111") == False
    assert is_valid("AA11AA") == False
    assert is_valid("111AAA") == False
    assert is_valid("AAA 11") == False
    assert is_valid("AAA_11") == False
    assert is_valid("AAA.11") == False
