import string
import random
import ctypes

nMinChar = (int)(input("Number of minimum characters:"))
nMaxChar = (int)(input("Number of maximum characters:"))
nSymbols = (int)(input("Number of Symbols:"))

nChar = random.randint(nMinChar, nMaxChar)

password = ""
nSymbol=0
chars = string.ascii_letters + string.digits
charsAndSymbols = chars + string.punctuation

for i in range(1,nChar+1):
    if(nSymbol < nSymbols):
        char = charsAndSymbols[random.randint(0, len(charsAndSymbols))]
        password+=char
        
        if(char in string.punctuation):
            nSymbol+=1
    else:
        char = chars[random.randint(0, len(chars))]
        password+=char

print(password)