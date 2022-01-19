from hangman_art import stages, logo
from hangman_words import word_list
import random


def printWord(chars,word):
    count = 0;
    for l in word:
        if(l in chars):
            print(l,end='')
            count+=1
        else: print(" _ ",end='')
    print("\n\n")
    return count


print(logo)

#Variables
word = word_list[random.randint(0, len(word_list)-1)].lower()
incorrect = []
correct = []
guesses = len(stages)-1
notFinished = True

#Main
while(notFinished):
    letter = input("Guess one letter: ").lower()

    if(letter in word):
        correct.append(letter)
    else: 
        guesses-=1
        incorrect.append(letter)

    print(stages[guesses])
    count = printWord(correct,word) 
    print("Incorrect answers: ["+ ', '.join(incorrect)+"]")
    notFinished = guesses != 0 and count != (len(word)) 

if(guesses != 0):
    print("Won")
else: 
    print("Lost. The word was: "+ word)