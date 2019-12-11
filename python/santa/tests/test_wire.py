from santa.wires import Wire, norm

def test_wire():
    ex = [("R8,U5,L5,D3", "U7,R6,D4,L4", 6, 30),
          ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159, 610),
          ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135, 410)]
    for desc1, desc2, exp_dist, exp_walk in ex:
        wire1 = Wire(desc1.split(","))
        wire2 = Wire(desc2.split(","))
        intersections = wire1.intersect(wire2)
        min_dist = min(norm(coord) for coord in intersections)
        min_walk = min(len(wire1.walk(coord)) + len(wire2.walk(coord)) - 2 for coord in intersections)
        assert min_dist == exp_dist
        assert min_walk == exp_walk
