# Characters Length
# Function that counts the number of characters in a file (It was useful when I was coding Tiles II)

path = r"C:\Users\imgog\AppData\LocalLow\ImGogole\Tiles II\Maps"
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
for element in onlyfiles :
    text = open(join(path, element), 'r').read()
    print(f"{element}'length is {len(text)} characters.")
