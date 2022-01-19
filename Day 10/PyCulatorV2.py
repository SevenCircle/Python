import os
import re


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    return a / b


def getValues(vals):
    count = 0
    toCalc = {}
    for val in vals:
        toCalc[count] = val
        count += 1
    return toCalc


def getDictionary(txt):
    toCalc = {}
    vals = [int(s) for s in re.split(', |_|-|!|\+|\*|\/', txt) if s.isdigit()]
    toCalc["values"] = getValues(vals)
    vals = ''.join([i for i in txt if not i.isdigit()])
    toCalc["operations"] = getValues(vals)

    return toCalc


def sortOperations(values, operators, count, maxVal, sortedValues):
    for val in values:
        if(values[val] == operators[count]):
            sortedValues[val] = values[val]

    if(count < maxVal-1):
        sortedValues = sortOperations(
            values, operators, count+1, maxVal, sortedValues)
    return sortedValues


values = getDictionary(input("Operation: "))

if(len(values['values']) > len(values['operations'])):
    sortedOps = sortOperations(
        values['operations'], "*/+-", 0, len("*/+-"), {})
    key = list(sortedOps.keys())[0]
    result = values['values'][key]
    # result = 0
    for op in sortedOps:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(values['values'])
        print("op: "+op)
        print("key: "+key)
        if(values['operations'][op] == '+'):
            result = addition(result, values['values'][op])
        elif(values['operations'][op] == '-'):
            result = subtraction(result, values['values'][op])
        elif(values['operations'][op] == '*'):
            result = multiple(result, values['values'][op])
        elif(values['operations'][op] == '/'):
            result = divide(result, values['values'][op])

    print(result)
