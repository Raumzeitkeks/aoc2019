from santa.intcode import IntCode
import itertools as itt

### input ###

with open('input/day7.txt') as f:
    code = [int(x) for x in f.readline().strip().split(",")]


### helper ###

def amplify(ics, input):
    signal = input
    for ic in itt.cycle(ics):
        ic.push(signal)
        ic.run(1)
        try:
            signal = ic.pop()
        except ic.HasNoOutput:
            break
    return signal


def maximize(amp_code, phases):
    max_seq = None
    max_thrust = 0
    for seq in itt.permutations(phases):
        ics = [IntCode(amp_code, [phase]) for phase in seq]
        thrust = amplify(ics, 0)
        if thrust > max_thrust:
            max_seq = seq
            max_thrust = thrust
    return max_seq, max_thrust


### solver ###

def solve_a():
    seq, thrust = maximize(code, range(5))
    return thrust


def solve_b():
    seq, thrust = maximize(code, range(5, 10))
    return thrust


### tests ###

def test_examples():
    ex = [(range(5), [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0], 43210),
          (range(5), [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4], 54321),
          (range(5), [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2], 65210),
          (range(5, 10), [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5], 139629729),
          (range(5, 10), [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], [9,7,8,5,6], 18216)]
    for phases, amp_code, opt_seq, max_thrust in ex:
        seq, thrust = maximize(amp_code, phases)
        print(amp_code)
        assert list(seq) == opt_seq
        assert thrust == max_thrust


def test_solution():
    assert solve_a() == 67023
    assert solve_b() == 7818398


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)