import turtle

def makeFlower(numberOfPetals):
     for _ in range(numberOfPetals):
        timmy.circle(100)
        timmy.left(360/numberOfPetals)


timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.shape("turtle")
# timmy.forward(100)

makeFlower(10)

screen.exitonclick()