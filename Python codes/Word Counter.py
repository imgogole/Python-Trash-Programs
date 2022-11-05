# Word Counter
# Get the amount of word on a text file. (Written this program because we had to count the number of words this way for our french DM and I was lazy to do it myself.)

FileName = "<YOUR-FILE-NAME>.txt"

Texte = open(FileName, "r").read();

def WordCount(text: str) :
    wordcount = 0
    isword = False

    alphas = "abcdefghijklmnopqrstuvwxz" + "éèùàëïêîâôç" # Only if non-ASCII
    alphas = alphas + alphas.upper()

    for char in text :
        if char in alphas :
            isword = True
        else :
            if isword :
                isword = False
                wordcount += 1
    if isword : wordcount += 1
    return wordcount

print(f"Number of word : {WordCount(Texte)}")