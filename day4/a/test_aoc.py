import santalib as santa 

def test_aoc_examples():
    assert santa.check(111111)
    assert not santa.check_increasing(223450)
    assert not santa.check_doubled(123789)

def test_my_examples():
    assert not santa.check_digits(11111)
    assert not santa.check_digits(1111111)
    assert santa.passwords(99990, 111113) == [111111, 111112]