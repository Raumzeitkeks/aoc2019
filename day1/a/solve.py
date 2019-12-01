import santalib as santa

with open("input.txt") as f:
	data = [int(l) for l in f]
	
mass = data
fuel = [santa.fuel(m) for m in mass]

for m, f in zip(mass, fuel):
	print(m, f)
	
print("total fuel:", sum(fuel))
