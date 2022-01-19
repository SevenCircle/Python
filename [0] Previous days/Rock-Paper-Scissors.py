import random

# def printHand(status):
#     match status:
#         case 0:
#             return '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#         case 1:
#             return '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#         case 2:
#             return  '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#         case _:
#             return "that is something funky that is not admissable in this court"


hands = [ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

, '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

, '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]


pcInput = random.randint(0, 2)
userInput = (int)(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))

if(userInput>2 or userInput<0):
    print("Nope try again!")
else:
    print(hands[userInput])
    print("Computer chose:")
    print(hands[pcInput])


    if((pcInput==0 and userInput==1) 
        or (pcInput==1 and userInput==2) 
        or (pcInput==2 and userInput==0)):
        print("You won")
    elif((pcInput==1 and userInput==0) 
        or (pcInput==2 and userInput==1) 
        or (pcInput==0 and userInput==2)):
        print("You Lost")
    else :
        print("Its a draw")
