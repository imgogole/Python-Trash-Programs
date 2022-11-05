# Transistors Destroyer
# Generates a huge file. Destroys your RAM and possibly your hard disk.

from random import randint

print("Starting")

# Destroying RAM

Data = ""
for _ in range(2**32) :
    Data += chr(randint(97, 122))

# Destroying hard disk

File = open("BigFileMotherfucker.txt", "w")
File.write(Data)
File.close()

print("Finished (enjoy)")
