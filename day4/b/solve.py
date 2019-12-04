import santalib as santa

with open("input.txt") as f:
	xmin, xmax = f.readline().split("-")

xmin, xmax = int(xmin), int(xmax)

pw_list = santa.passwords(xmin, xmax)

print(len(pw_list))