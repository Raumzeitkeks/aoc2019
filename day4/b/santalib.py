
def check_digits(x):
    return 99999 < x < 1000000

def check_twice(x):
    return any(str(x).count(d) == 2 for d in "123456789")
    
def check_increasing(x):
    return sorted(str(x)) == list(str(x))

def check(x):
    return check_digits(x) and check_twice(x) and check_increasing(x)

def passwords(xmin, xmax):
    return [x for x in range(xmin, xmax) if check(x)]
    