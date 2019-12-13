
### input ###

with open('input/day4.txt') as f:
    x_min, x_max = [int(x) for x in f.readline().split("-")]


### helper ###

def six_digits(x):
    return 99999 < x < 1000000

def multi_occurence(x):
    return len(set(str(x))) < len(str(x))

def double_occurence(x):
    return any(str(x).count(d) == 2 for d in "123456789")

def non_decreasing(x):
    return sorted(str(x)) == list(str(x))

def valid_a(x):
    return six_digits(x) and multi_occurence(x) and non_decreasing(x)

def valid_b(x):
    return six_digits(x) and double_occurence(x) and non_decreasing(x)


### solver ###

def solve_a():
    pwlist = [x for x in range(x_min, x_max) if valid_a(x)]
    print(pwlist)
    return len(pwlist)


def solve_b():
    pwlist = [x for x in range(x_min, x_max) if valid_b(x)]
    print(pwlist)
    return len(pwlist)


### tests ###

def test_units():
    assert six_digits(123456)
    assert not six_digits(12345)
    assert not six_digits(1234567)
    
    assert multi_occurence(1123)
    assert multi_occurence(1223)
    assert multi_occurence(1233)
    assert multi_occurence(112233)
    assert multi_occurence(12223)
    assert not multi_occurence(123)
    
    assert double_occurence(1123)
    assert double_occurence(1223)
    assert double_occurence(1233)
    assert double_occurence(112233)
    assert not double_occurence(123)
    assert not double_occurence(12223)
    
    assert non_decreasing(1)
    assert non_decreasing(1234)
    assert non_decreasing(125)
    assert not non_decreasing(1324)


def test_examples():
    assert valid_a(111111)
    assert not valid_a(223450)
    assert not valid_a(123789)
    
    assert valid_b(112233)
    assert not valid_b(123444)
    assert valid_b(111122)


def test_solution():
    assert solve_a() == 2050
    assert solve_b() == 1390


### main ###

if __name__ == "__main__":
    print("----- a -----")
    a = solve_a()
    print("----- b -----")
    b = solve_b()
    print("----- result -----")
    print("a:", a)
    print("b:", b)