import string
import random
import ctypes
from os.path import exists

nMinChar = (int)(input("Number of minimum characters:"))
nMaxChar = (int)(input("Number of maximum characters:"))
nSymbols = (int)(input("Number of Symbols:"))
placeholder = input("Password of: ")

nChar = random.randint(nMinChar, nMaxChar)

password = ""
nSymbol = 0
chars = string.ascii_letters + string.digits
charsAndSymbols = chars + string.punctuation

for i in range(nChar):
    if(nSymbol < nSymbols):
        char = charsAndSymbols[random.randint(0, len(charsAndSymbols)-1)]
        password += char

        if(char in string.punctuation):
            nSymbol += 1
    else:
        char = chars[random.randint(0, len(chars)-1)]
        password += char

path = r'/home/sevencircle/Documents/Python/password.txt'
if(exists(path)):
    passFile = open(path, 'a')
else:
    passFile = open(path, 'w')

passFile.write('[ '+placeholder+' ] --> [ ' + password + ' ]\n')
