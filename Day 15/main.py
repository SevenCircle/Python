import data


def report():
    for res in data.resources:
        if res.lower() == "coffee":
            sign = "g"
        elif res.lower() == "money":
            sign = ""
        else:
            sign = "ml"

        if res.lower() == "money":
            dollarsign = "$"
        else:
            dollarsign = ""

        print(res+f": {dollarsign}"+str(data.resources[res])+f"{sign}")


def turnOff():
    data.OffSwitch = True


def turnOn():
    data.OffSwitch = False


def checkResources(answer):
    for ingr in data.MENU[answer]["ingredients"]:
        if(data.resources[ingr] < data.MENU[answer]["ingredients"][ingr]):
            print(f"Sorry there is not enough {ingr}.")
            return False
    return True


def machineOff(answer):
    if(answer == 'on'):
        turnOn()
    elif (answer == 'off'):
        return True
    elif (answer == 'refill' or answer == 'refuel'):
        refill()
    else:
        print("Machine is turned down, no procedures can be made")

    return False


def askForMoney(answer):
    val = 0
    mult = "NaN"
    for coin in data.coins:
        while not mult.isdecimal():
            mult = input(f"How many {coin}? ")
            if not mult.isdecimal():
                print("Must be a number")
        val += data.coins[coin] * int(mult)
        mult = "NaN"

    data.resources["Money"] = val
    return data.MENU[answer]["cost"] <= val


def getChange(answer):
    return round(data.resources["Money"] - data.MENU[answer]["cost"], 2)


def useMaterials(answer):
    for ingr in data.MENU[answer]["ingredients"]:
        data.resources[ingr] -= data.MENU[answer]["ingredients"][ingr]

    data.resources["Money"] = 0


def refill():
    print("Current Report")
    report()
    for res in data.resources:
        val = "NaN"
        if(res != "Money"):
            while not val.isdecimal():
                val = input(f"How much {res} you going to add:")
                data.resources[res] += int(val)
            val = "NaN"
    print("Updated Report")
    report()


def getProduct(answer):
    if(checkResources(answer)):
        if(askForMoney(answer)):
            print(f"Here is your {answer}", end='')
            change = getChange(answer)
            print(f" and the change is {change}" if change > 0 else "")
            useMaterials(answer)
        else:
            print("Sorry that's not enough money. Money refunded.")
            data.resources["Money"] = 0


def machineOn(answer):
    if(answer == 'off'):
        turnOff()
    else:
        getProduct(answer)


comOff = False
while not comOff:
    if(not data.OffSwitch):
        answer = input('What would you like? (espresso/latte/cappuccino):')
    else:
        answer = input('Machine is turned down:')

    if(answer == 'report'):
        report()

    if(answer in data.offCommands and data.OffSwitch):
        comOff = machineOff(answer)
    elif (answer in data.onCommands):
        machineOn(answer)
