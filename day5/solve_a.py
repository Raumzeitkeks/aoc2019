import santalib as santa

with open("input.txt") as f:
    data = f.readline()
code = [int(v) for v in data.split(",")]

ic = santa.IntCode(code, [1], print)
ic.run()
