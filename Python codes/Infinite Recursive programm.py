# Infinite Recursive programm
# Get free power


def func1() :
  return func2()
def func2() :
  return func1()
func1()
print("End")