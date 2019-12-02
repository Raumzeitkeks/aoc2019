import santalib as santa

with open("input.txt") as f:
	data = f.readline()
	
original_code = data.split(",")

def solve():
	for noun in range(0, 100):
		for verb in range(0, 100):
			code = original_code.copy()
			code[1] = noun
			code[2] = verb
			ic = santa.IntCode(code)
			ic.run()
			if ic[0] == 19690720:
				return noun, verb
	
print(solve())
