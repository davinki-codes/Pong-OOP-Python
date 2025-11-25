from turtle import Turtle

DISTANCE = 20  # how far paddle moves per key press

LEFT = (-290, 0)
RIGHT = (280, 0)

class Paddle:
    def __init__(self, position):
        self.my_paddle = Turtle("square")
        self.my_paddle.color("white")
        self.my_paddle.shapesize(stretch_wid=5, stretch_len=1)  # tall paddle
        self.my_paddle.penup()

        if position == 'left':
            self.my_paddle.goto(LEFT)
        elif position == 'right':
            self.my_paddle.goto(RIGHT)

    def up(self):
        y = self.my_paddle.ycor() + DISTANCE
        if y < 280:  # keep inside top boundary
            self.my_paddle.sety(y)

    def down(self):
        y = self.my_paddle.ycor() - DISTANCE
        if y > -280:  # keep inside bottom boundary
            self.my_paddle.sety(y)