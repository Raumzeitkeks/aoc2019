import santalib as santa 

def test_aoc_examples():
	assert santa.fuel(12) == 2
	assert santa.fuel(14) == 2
	assert santa.fuel(1969) == 654
	assert santa.fuel(100756) == 33583
