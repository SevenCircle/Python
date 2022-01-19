import os


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    return a / b


def getNumber(text):
    while True:
        val = input(text)
        if(val.isdecimal()):
            return int(val)


close = False
a = {}
while not close:
    os.system('cls' if os.name == 'nt' else 'clear')
    if(not bool(a)):
        a = getNumber("What is the first number? ")
    b = getNumber("What is the second number? ")

    print("What operation should you do?")
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("")[0]
    result = {}
    match operation:
        case "+":
            a = addition(a, b)
        case "-":
            a = subtraction(a, b)
        case "*":
            a = multiple(a, b)
        case "/":
            a = divide(a, b)
    print("Result: " + str(a))

    close = input("Close? (y/n) ").lower()[0] == "y"
