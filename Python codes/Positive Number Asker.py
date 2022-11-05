# Positive Number Asker
# Function that asks the user to enter a positive number. Not useful, I still wonder why I wrote this code...

def GetPositiveNumberInput(Message) :
    Number = -1
    while Number < 0 :
        try :
            Input = input(Message)
            Number = int(Input)
        except :
            print("Please enter a positive number.")
            Number = -1
    return Number

a = GetPositiveNumberInput("Enter a positive number : ")
    
