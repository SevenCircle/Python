MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0.0
}

coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.10,
    "quarters": 0.25
}

OffSwitch = False
onCommands = ["off","espresso","latte","cappuccino"]
offCommands = ["on", "off", "refuel","refill"]