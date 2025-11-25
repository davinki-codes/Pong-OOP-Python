from turtle import Turtle
import random

DISTANCE = 10
ANGLES = [0,30,60,120,150,180,210,240,300,330,360] # NO 90 AND 270

TOP_WALL = 270
BOTTOM_WALL = -270

LEFT_SCOREBOARD = (-50, 190)
RIGHT_SCOREBOARD = (50, 190)
ROUND_NUMBERS_DISPLAY = (-90,240)

FONT = ('Arial', 40, 'normal')

class Pong:
    def __init__(self):
        self.ball = Turtle(shape ='circle') #assign this - its now a set guy. that can be accessed whenever someone starts pong class
        self.setup()
        self.start()

    def setup(self):
        self.ball.color('white')
        self.ball.shapesize(stretch_wid=1, stretch_len=1)
        self.ball.penup()

    def start(self):
        self.ball.goto(0, 0)
        self.ball.setheading(random.choice(ANGLES))
        self.ball.speed = 0.08

    def refresh(self):
        self.ball.hideturtle()
        self.start()
        self.ball.showturtle()

    def move(self):
        self.ball.forward(DISTANCE)

    def bounce_wall(self):
        current_heading = self.ball.heading()
        self.ball.setheading(-current_heading)  # reflects vertically

    def bounce_paddle(self):
        current_heading = self.ball.heading()
        self.ball.setheading(180 - current_heading)  # reflects horizontally
        self.ball.speed *= 0.5


class Pong_Scoreboard():

    def __init__(self):
        self.left_scorer = Turtle()
        self.right_scorer = Turtle()
        self.left_score = 0
        self.right_score = 0
        self.scorer()  # sets up both turtles at correct positions

        self.round = 1
        self.round_turtle = Turtle()
        self.round_turtle.color('white')

    def scorer(self):
        for p in (self.left_scorer, self.right_scorer):
            p.color('white')
            p.hideturtle()
            p.penup()
        self.left_scorer.goto(LEFT_SCOREBOARD)
        self.right_scorer.goto(RIGHT_SCOREBOARD)
        self.update_score()

    def update_score(self):
        self.left_scorer.clear()
        self.left_scorer.write(f'{self.left_score}', font=FONT)
        self.right_scorer.clear()
        self.right_scorer.write(f'{self.right_score}', font= FONT)

    def l_point(self):
        self.left_score += 1
        self.update_score()

    def r_point(self):
        self.right_score += 1
        self.update_score()

    def cal_rounds(self):
        self.round_turtle.hideturtle()
        self.round_turtle.penup()
        self.round_turtle.goto(ROUND_NUMBERS_DISPLAY)
        self.round_turtle.clear()
        self.round_turtle.write(f'Round: {self.round}', font = FONT)

        self.round += 1

    def game_over(self):
        self.round_turtle.clear()
        self.round_turtle.goto(x=-200,y=50)
        if self.right_score < self.left_score:
            winner = 'PLAYER 1 WINS'
        elif self.right_score > self.left_score:
            winner = 'PLAYER 2 WINS'
        else:
            winner = 'IT IS A TIE :('

        self.round_turtle.write(f'GAME OVER\n{winner}', font = FONT)



 # p.shapesize(stretch_wid=2, stretch_len=0.5)