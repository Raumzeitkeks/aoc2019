import santalib as santa 

def test_aoc_examples():
	assert santa.fuel(14) == 2
	assert santa.fuel(1969) == 966
	assert santa.fuel(100756) == 50346
