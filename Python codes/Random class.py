# Random class
# I created my own random class with the linear congruential generator.

import math

class Random :
    NewSeed = 52626
    def __init__(self, Seed = None) :
        if Seed == None :
            Seed = Random.NewSeed
        self.__InitialSeed = Seed
        self.__CurrentSeed = Seed

        self.__M = 10 ** 8
        self.__C = 1
        self.__A = 31415821
    def Next(self, Start = 0, End = 1) :
        return math.floor(Start + self.__GetNext() * (End - Start))
    def __GetNext(self) :
        self.__CurrentSeed = (self.__A * self.__CurrentSeed + self.__C) % self.__M
        Random.NewSeed = self.__CurrentSeed
        return round(self.__CurrentSeed / self.__M, 8)

random = Random()
for _ in range (25) :
	print(random.Next(0,5))
