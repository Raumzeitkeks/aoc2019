
def check_digits(x):
    return 99999 < x < 1000000

def check_doubled(x):
    return len(set(str(x))) < len(str(x))
    
def check_increasing(x):
    return sorted(str(x)) == list(str(x))

def check(x):
    return check_digits(x) and check_doubled(x) and check_increasing(x)

def passwords(xmin, xmax):
    return [x for x in range(xmin, xmax) if check(x)]
    