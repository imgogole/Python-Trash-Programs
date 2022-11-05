# Fast Expo
# Get the result of B^N (for N whole relative number)

def Exponential(Base, Exp) :
    if Base == 0 :
        return 0
    if Base == 1 or Exp == 0 :
        return 1
    if Exp == 1 :
        return Base
    if Exp == 2 :
        return Base * Base

    if Exp < 0 :
        return 1 / Exponential(Base, -Exp)

    if 0 < Exp < 1 :
        pass # To complete

    IsExpEven = Exp % 2 == 0

    if IsExpEven :
        return Exponential(Exponential(Base, Exp // 2), 2)
    else :
        return Exponential(Exponential(Base, Exp // 2), 2) * Base

print(Exponential(8.5, -6.99669))
