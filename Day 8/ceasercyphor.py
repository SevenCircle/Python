import string
from string import ascii_lowercase as letters

def greet():
    return input('Do you want to encode or decode? [(e)ncode/(d)ecode/e(x)it]')


def cypher(letter, shift):
    if(letter.isalpha()):
        anchor = letters.index(letter)
        shift = anchor + shift;
        if(shift < len(letters)):
            return letters[shift]
        else :
            return letters[shift- len(letters)]

    else: return letter

def decypher(letter, shift):
    if(letter.isalpha()):
        return letters[letters.index(letter) - shift]
    else: return letter

def encodeOrDecode(method):
    if method == 'x':
        return True
   
    toEncode = input('Encode: ').lower()
    shift = input('Shift: ')
    if(shift.isdecimal()):
        shift = int(shift)
    else:
        print("Shift must be a number")
        return False

    aux = ""
    for l in toEncode:
        if(method == "e" or method == "encode"):
            aux+=cypher(l,shift)
        elif(method == "d" or method == "decode"): 
            aux+=decypher(l,shift)
    print(aux)
    
    return False


close=False;
while not close:
    method = greet()
    print(letters)
    close = encodeOrDecode(method)