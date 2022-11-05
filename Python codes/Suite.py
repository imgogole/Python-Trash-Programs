# Suite
# Definitely a program I did in Première for a crappy math test

def Suite(time) :
    un = 4
    summ = 0
    for _ in range(time) :
        summ += un
        un += 2.5
    summ += un
    return un, summ

print(Suite(65), Suite(24))
print(Suite(65)[1] - Suite(24)[1])
