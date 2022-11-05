# Index Converter

# Okey this is very effective. Imagine a MxN grid, and elements are sorted from the bottom-right to the top-left. So basically,
# if the first element is 0 (bottom-right), to convert it into a coordinate that the corner is the origin, you can use IndexToCoords
# to get these coordinates (Index is the rank of the element, Base is a MxN vector, the grid size)

#   Grid of 10x10 (M=10, N=10)
#
#      N
#    9 |9  19 29                   100 
#    8 |8  18 28                   ..
#    7 |7  17 27 
#    6 |6  16 26
#    5 |5  15 25 ..
#    4 |4  14 24 ..
#    3 |3  13 23 33
#    2 |2  12 22 32
#    1 |1  11 21 31
#    0 |0  10 20 30
#       __ __ __ __ __ __ __ __ __ __ M
#       0  1  2  3  4  5  6  7  8  9  
#
#   For instance 26 is in coordinates (x= 2; y= 6)
#   So 26 = x * N + y = 2 * 10 + 6


class Vector2 :
    def __init__(self, x = 0, y = 0) :
        self.x = x
        self.y = y
    def Magnitude(self) :
        return (self.x ** 2 + self.y ** 2)


def CoordsToIndex(Coords, Base) :
    if (Coords.Magnitude() > Base.Magnitude()) : return -1;
    if (Coords.x > Base.x or Coords.x < 0) : return -1;
    if (Coords.y > Base.y or Coords.y < 0) : return -1;

    return Coords.x * Base.x + Coords.y

def IndexToCoords(Index, Base) :
    if (CoordsToIndex(Base, Base) < Index) : return Vector2(-1, -1) 
    vector = Vector2(Index // Base.y, Index % Base.y)
    return vector

Base = Vector2(10, 15)
