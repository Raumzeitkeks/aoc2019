import santalib as santa

with open("input.txt") as f:
	data = [line.strip().split(")") for line in f]
	
uom = santa.OrbitMap()

for center, satellit in data:
    uom.add_orbit(center, satellit)
    
print(uom.checksum())
