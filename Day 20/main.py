from turtle import Screen
from snake import Snake
from apple import Apple
import constants
import time
import random

def getApple(snake):
    apple = (random.randint(0,constants.SCREENX/10)*10, random.randint(0,constants.SCREENY/10)*10)
    if(snake.isInBody(apple)):
        apple = getApple(snake)
    return apple


# Screen
screen = Screen()
screen.listen()
screen.screensize(constants.SCREENX, constants.SCREENY)
screen.bgcolor("black")

snake = Snake()
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")

apple = Apple(getApple(snake))


while(True):
    snake.moveBody()
    time.sleep(0.01)

screen.exitonclick()
