import santalib as santa 

def test_aoc_examples():
    examples = [
            ("R8,U5,L5,D3", "U7,R6,D4,L4", 6, 30),
            ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159, 610),
            ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135, 410)
            ]
    for path_a, path_b, aoc_min_dist, aoc_min_walk in examples:
        path_a = path_a.split(",")
        path_b = path_b.split(",")
        trace_a = santa.trace(path_a)
        trace_b = santa.trace(path_b)
        intersections = santa.intersect(trace_a, trace_b)
        min_dist = min(santa.norm(coord) for coord in intersections)
        min_walk = min((santa.walk(trace_a, coord) + santa.walk(trace_b, coord)) for coord in intersections)
        assert min_dist == aoc_min_dist
        assert min_walk == aoc_min_walk
        