# Random class (Turing version)
# Random class with Turing algorithm (basically shit)

seed = 6532

def TakeMiddle(number, count = 4) :
    print("Given seed :", number)
    lenNumber = len(str(number))
    print("Number's length :", lenNumber)
    if lenNumber <= count :
        return number
    lenExtremity = (len(str(number)) - count) / 2
    print("Extremity's length :", lenExtremity)
    if lenExtremity > 0 :
        if lenExtremity.is_integer() :
            lenExtremity = int(lenExtremity)
            returnedNumber = str(number)[lenExtremity::]
            returnedNumber = returnedNumber[:lenExtremity:]
            return int(returnedNumber)
        else :
            firstcase = int(lenExtremity)
            secondcase = int(lenExtremity) + 1
            mystr = str(number)[:-1:]
            returnedNumber = mystr[firstcase::]
            returnedNumber = returnedNumber[:-secondcase:]
            return int(returnedNumber)

def GenerateNumber() :
    global seed
    newSeed = seed

    newSeed = newSeed ** 2

    seed = TakeMiddle(newSeed)

    return seed

print(GenerateNumber())

    
