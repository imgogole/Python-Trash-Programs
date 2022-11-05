# Binary To ASCII
# Loop converting any input (binary or ASCII) into ASCII or binary.

while True :
    Input = input("Enter your input (Start it with \"b\" if it's binary or \"t\" if it's ASCII text) : ")

    if Input[0].lower() == "b":
        Input = Input[2:]
        Result = ""
        for char in Input :
            Result += bin(ord(char)*2)[2:] + " "
        print(Result)
    if Input[0].lower() == "t" :
        Input = Input[2:].split(" ")
        Result = ""
        for binary in Input:
            Result += chr(int(binary, 2)//2)
        print(Result)
