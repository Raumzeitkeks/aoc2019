from santa.orbitmap import OrbitMap

### input ###

with open('input/day6.txt') as f:
    orbits = [line.strip() for line in f]


### solver ###

def solve_a():
    uom = OrbitMap("COM", orbits)
    return uom.checksum()


def solve_b():
    uom = OrbitMap("COM", orbits)
    return uom.transfers(uom.center("YOU"), uom.center("SAN"))


### tests ###

def test_solution():
    assert solve_a() == 224901
    assert solve_b() == 334


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)