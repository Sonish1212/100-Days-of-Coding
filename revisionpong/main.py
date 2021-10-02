from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('The pong game')
screen.tracer(0)

r_paddle = Paddle()
r_paddle.goto(350, 0)
l_paddle = Paddle()
l_paddle.goto(-350, 0)

ball = Ball()

score_board = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_backward, "Down")

screen.listen()
screen.onkey(r_paddle.move_forward, "Up")

screen.listen()
screen.onkey(l_paddle.move_backward, "s")

screen.listen()
screen.onkey(l_paddle.move_forward, "w")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.bounce_x()

    if ball.xcor() > 340:
        ball.refresh()
        score_board.r_point()
        ball.move_speed = 0.1

    if ball.xcor() < -340:
        ball.refresh()
        score_board.l_point()
        ball.move_speed = 0.1


screen.exitonclick()