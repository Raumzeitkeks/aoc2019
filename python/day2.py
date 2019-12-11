from santa.intcode import IntCode

### input ###

with open('input/day2.txt') as f:
    code = [int(x) for x in f.readline().strip().split(",")]


### solver ###

def solve_a():
    code[1:3] = 12, 2
    ic = IntCode(code)
    ic.run()
    print(ic.dump())
    return ic.dump()[0]


def solve_b():
    for noun in range(0, 100):
        for verb in range(0, 100):
            code[1:3] = noun, verb
            ic = IntCode(code)
            ic.run()
            dump = ic.dump()
            result = dump[0]
            print(ic.dump())
            print("noun:", noun, "verb:", verb, "result:", result)
            if result == 19690720:
                return 100 * noun + verb


### tests ###

def test_solution():
    assert solve_a() == 4330636
    assert solve_b() == 6086


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)