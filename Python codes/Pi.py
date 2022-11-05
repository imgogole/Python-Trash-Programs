# Pi
# Get the approximation of pi

def part(i, n) :
    return n / (n ** 2 + i ** 2)

def pi(floatingPointPrecision) :
    pi = 0
    for i in range(floatingPointPrecision) :
        pi += part(i, floatingPointPrecision)
    return 4 * pi
