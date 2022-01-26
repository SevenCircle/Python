from turtle import Turtle, Screen
import random

turtles = [
    Turtle("turtle"),
    Turtle("turtle"),
    Turtle("turtle"),
    Turtle("turtle"),
    Turtle("turtle"),
]


def moveTurtle():
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if(turtle.pos()[0]+distance >= 230):
            return turtle

    return -1


colors = ["red", "blue", "green", "yellow", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("make your bet", "Turtle that will win the race")
i = 160
count = 0
for turtle in turtles:
    turtle.penup()
    turtle.color(colors[count])
    turtle.goto(-230, i)
    i -= 80
    count += 1

finished = False
while not finished:
    value = moveTurtle()
    finished = value != -1

if(bet.lower() == value.color()[0]):
    print("You win!")
else: print(f"You loose for the {value.color()[0]}")

screen.exitonclick()
