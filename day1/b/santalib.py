def fuel(mass):
	total_fuel = 0
	fuel = mass//3 - 2
	while fuel > 0:
		total_fuel += fuel
		fuel = fuel//3 - 2
	
	return total_fuel
