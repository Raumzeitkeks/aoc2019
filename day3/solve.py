import santalib as santa

with open("input.txt") as f:
	path_a = f.readline().split(",")
	path_b = f.readline().split(",")
	
trace_a = santa.trace(path_a)
trace_b = santa.trace(path_b)

intersections = santa.intersect(trace_a, trace_b)

min_dist = min(santa.norm(coord) for coord in intersections)
min_walk = min((santa.walk(trace_a, coord) + santa.walk(trace_b, coord)) for coord in intersections)

print(min_dist, min_walk)
