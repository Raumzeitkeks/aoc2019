import santalib as santa 

def test_aoc_examples():
    assert santa.check(112233)
    assert not santa.check(123444)
    assert santa.check(111122)

def test_my_examples():
    assert not santa.check_digits(11111)
    assert not santa.check_digits(1111111)
    assert not santa.check_twice(1112)
    assert santa.check_twice(1212)
    assert santa.passwords(99990, 111140) == [111122, 111133]