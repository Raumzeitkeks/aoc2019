from santa.intcode import IntCode

### input ###

with open('input/day7.txt') as f:
    code = [int(x) for x in f.readline().strip().split(",")]


### helper ###

def input(iterable):
    it = iter(iterable)
    def _gen():
        return next(it)
    return _gen


def maximize(a_in, phases):
    max_seq = None
    max_thrust = 0
    for a in phases:
        a_out = []
        a_ic = IntCode(code, input([a, a_in]), a_out.append)
        a_ic.run()
        b_in = a_out[0]
        for b in set(phases).difference([a]):
            b_out = []
            b_ic = IntCode(code, input([b, b_in]), b_out.append)
            b_ic.run()
            c_in = b_out[0]
            for c in set(phases).difference([a, b]):
                c_out = []
                c_ic = IntCode(code, input([c, c_in]), c_out.append)
                c_ic.run()
                d_in = c_out[0]
                for d in set(phases).difference([a, b, c]):
                    d_out = []
                    d_ic = IntCode(code, input([d, d_in]), d_out.append)
                    d_ic.run()
                    e_in = d_out[0]
                    for e in set(phases).difference([a, b, c, d]):
                        e_out = []
                        e_ic = IntCode(code, input([e, e_in]), e_out.append)
                        e_ic.run()
                        thrust = e_out[0]
                        if thrust > max_thrust:
                            max_seq = [a, b, c, d, e]
                            max_thrust = thrust
    return max_seq, max_thrust

### solver ###

def solve_a():
    seq, thrust = maximize(0, range(5))
    return thrust


def solve_b():
    pass


### tests ###

def test_examples():
    ex = [([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0], 43210),
          ([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4], 54321),
          ([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2], 65210)]
    for code, opt_seq, max_thrust in ex:
        pass


def test_solution():
    assert solve_a() == None
    assert solve_b() == None


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)