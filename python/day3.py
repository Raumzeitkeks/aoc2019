from santa.wires import Wire, norm

### input ###

with open('input/day3.txt') as f:
    wire_descr_a = f.readline().strip().split(",")
    wire_descr_b = f.readline().strip().split(",")


### solver ###

def solve_a():
    wire_a = Wire(wire_descr_a)
    wire_b = Wire(wire_descr_b)
    intersections = wire_a.intersect(wire_b)
    print(intersections)
    min_dist = min(norm(coord) for coord in intersections)
    return min_dist


def solve_b():
    wire_a = Wire(wire_descr_a)
    wire_b = Wire(wire_descr_b)
    intersections = wire_a.intersect(wire_b)
    print(intersections)
    min_walk = min(len(wire_a.walk(coord)) + len(wire_b.walk(coord)) - 2 for coord in intersections)
    return min_walk


### tests ###

def test_solution():
    assert solve_a() == 5319
    assert solve_b() == 122514


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)