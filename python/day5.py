from santa.intcode import IntCode

### input ###

with open('input/day5.txt') as f:
    code = [int(x) for x in f.readline().strip().split(",")]


### solver ###

def solve_a():
    input = [1]
    ic = IntCode(code, input)
    ic.run()
    print(ic.output())
    return ic.output()[-1]


def solve_b():
    input = [5]
    ic = IntCode(code, input)
    ic.run()
    print(ic.output())
    return ic.output()[-1]


### tests ###

def test_solution():
    assert solve_a() == 15314507
    assert solve_b() == 652726


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)