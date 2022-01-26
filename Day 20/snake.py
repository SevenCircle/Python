from turtle import Turtle
from constants import Orientation

# Snake body
# Notes
# Segments are part of the body


class Snake:
    def __init__(self):
        self.segments = []
        self.orientation = Orientation.RIGHT
        for i in range(5):
            pos = [i * (-20), 0]
            self.grow(pos)

    # The Snake's body grows one time
    def grow(self, position):
        segment = Turtle(shape="square")
        segment._tracer(None, None)
        segment.penup()
        segment.color("white")
        segment.setpos(position[0], position[1])
        self.segments.append(segment)

    # Checks if it collides with itself
    # If Wall is true it will check collision with wall
    def checkCollition(self, wall):
        pass

    def isInBody(self, pos):
        for seg in self.segments:
            print(seg.pos())
            if(seg.pos() == pos):
                return True
        return False

    def moveUp(self):
        if self.orientation != Orientation.DOWN:
            self.orientation = Orientation.UP

    def moveLeft(self):
        if self.orientation != Orientation.RIGHT:
            self.orientation = Orientation.LEFT

    def moveRight(self):
        if self.orientation != Orientation.LEFT:
            self.orientation = Orientation.RIGHT

    def moveDown(self):
        if self.orientation != Orientation.UP:
            self.orientation = Orientation.DOWN

    # Moves the snake

    def move(self, orientation):
        x = self.segments[0].pos()[0]
        y = self.segments[0].pos()[1]
        if(orientation == Orientation.UP):
            self.segments[0].goto(x, y+10)
        elif(orientation == Orientation.DOWN):
            self.segments[0].goto(x, y-10)
        elif(orientation == Orientation.RIGHT):
            self.segments[0].goto(x+10, y)
        elif(orientation == Orientation.LEFT):
            self.segments[0].goto(x-10, y)

        for part in self.segments[1:]:
            auxX = part.pos()[0]
            auxY = part.pos()[1]

            part.goto(x, y)

            x = auxX
            y = auxY

    def moveBody(self):
        self.move(self.orientation)
