from santa.intcode import IntCode

### input ###

with open('input/day9.txt') as f:
    code = [int(x) for x in f.readline().strip().split(",")]


### solver ###

def solve_a():
    input = [1]
    ic = IntCode(code, input)
    ic.run()
    print(ic.output())
    return ic.output()[-1]


def solve_b():
    input = [2]
    ic = IntCode(code, input)
    ic.run()
    print(ic.output())
    return ic.output()[-1]


### tests ###

def test_solution():
    assert solve_a() == 2671328082
    assert solve_b() == 59095


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)