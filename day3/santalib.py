
def trace(path):
	x, y = 0, 0
	coords = []
	for instruction in path:
		direction = instruction[0]
		distance = int(instruction[1:])
		if direction == "U":
			coords.extend((x, y+i) for i in range(1, distance))
			y += distance
		elif direction == "D":
			coords.extend((x, y-i) for i in range(1, distance))
			y -= distance
		elif direction == "L":
			coords.extend((x-i, y) for i in range(1, distance))
			x -= distance
		elif direction == "R":
			coords.extend((x+i, y) for i in range(1, distance))
			x += distance
		coords.append((x, y))
	return coords

def intersect(trace_a, trace_b):
    intersections = set(trace_a).intersection(trace_b)
    return intersections

def norm(coord):
    return abs(coord[0]) + abs(coord[1])

def walk(trace, coord):
    return next(i+1 for i, c in enumerate(trace) if c == coord)
