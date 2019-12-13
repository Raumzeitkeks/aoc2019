
### input ###

with open("input/day1.txt") as f:
    masses = [int(line) for line in f]


### helper ###

def direct_fuel(mass):
    return mass//3 - 2


def indirect_fuel(mass):
    total = 0
    fuel = direct_fuel(mass)
    while fuel > 0:
        total += fuel
        fuel = direct_fuel(fuel)
    return total


### solver ###

def solve_a():
    fuel = [direct_fuel(m) for m in masses]
    total = sum(fuel)
    print(list(zip(masses, fuel)))
    print("total:", total)
    return total


def solve_b():
    fuel = [indirect_fuel(m) for m in masses]
    total = sum(fuel)
    print(list(zip(masses, fuel)))
    print("total:", total)
    return total


### tests ###

def test_examples():
    assert direct_fuel(12) == 2
    assert direct_fuel(14) == 2
    assert direct_fuel(1969) == 654
    assert direct_fuel(100756) == 33583
    assert indirect_fuel(12) == 2
    assert indirect_fuel(14) == 2
    assert indirect_fuel(1969) == 966
    assert indirect_fuel(100756) == 50346


def test_solution():
    assert solve_a() == 3296560
    assert solve_b() == 4941976


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)