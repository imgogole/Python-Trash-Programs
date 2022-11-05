# Log Rand Unit
# Function that generate a random normalized value (between zero and one) where there is more chance to get zero than one.
# Use mathematical functions to get your expected demand :

# Rescale the value ([0; 1] => [min; max]) : logRandUnit() * (max - min) + min
# Have more chance to get one than zero : 1 - logRandUnit()

from random import *
from math import *


def logRandUnit(p=100, e=2.7182818284590451) :
    unit = randint(0, p) + 1
    logunit = log(unit, e) / log(p, e)
    return abs(1 - logunit)

for _ in range(500):
    print(int(logRandUnit() * 50))
