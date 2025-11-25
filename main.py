from turtle import Screen
from paddle_setup import Paddle
from pong_and_score import Pong, Pong_Scoreboard
import time
from random import randint

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor('black')
screen.title('Pong')

left_paddle = Paddle('left')
right_paddle = Paddle('right')

pong = Pong()

screen.listen()
#assign keys for pong control
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

number_of_rounds = 3

scoreboard = Pong_Scoreboard()
scoreboard.cal_rounds()

game = True
while game:
    screen.update()
    time.sleep(pong.ball.speed)
    pong.move()

    #BOUCE OFF THE PADDLE
    if pong.ball.distance(right_paddle.my_paddle) <= 40 and pong.ball.xcor() > 260: # right paddle
        pong.bounce_paddle()

    if pong.ball.distance(left_paddle.my_paddle) <= 40 and pong.ball.xcor() < -270: # left paddle
        pong.bounce_paddle()

    #paddle miss
    if pong.ball.xcor() > 320 or pong.ball.xcor() < -320 :
        if pong.ball.xcor() > 320:
            scoreboard.l_point()

        if pong.ball.xcor() < -320:
            scoreboard.r_point()

        pong.refresh() #resets the position
        scoreboard.cal_rounds()

    #bounce walls
    if pong.ball.ycor() > 280 or pong.ball.ycor() < -280:
        pong.bounce_wall()

    if scoreboard.round - 1 > number_of_rounds:
        pong.ball.clear()
        scoreboard.game_over()
        game = False









screen.exitonclick()
