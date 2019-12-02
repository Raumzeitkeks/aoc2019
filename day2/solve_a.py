import santalib as santa

with open("input.txt") as f:
	data = f.readline()
	
code = data.split(",")
code[1] = 12
code[2] = 2

ic = santa.IntCode(code)
ic.run()
	
print(list(ic))
