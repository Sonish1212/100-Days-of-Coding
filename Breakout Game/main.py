from turtle import Screen
from paddle import Paddle
from block import Block, Block2, Block3
from ball import Ball
import time
import random

screen = Screen()
screen.title("Breakout Game(80's Game)")
screen.setup(width=800, height=600)
screen.bgcolor("black")

game_paddle = Paddle((0, -280))
game_paddle.color('red')

x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [240, 215, 190, 165, 140]
block_list = []
colors = ['red', 'blue', 'green', 'cyan', 'purple', 'yellow', 'orange']
for i in y_list:
    for j in x_list:
        block = Block((j,i))
        block.shape('square')
        block.shapesize(stretch_len=5, stretch_wid=1)
        block.color(random.choice(colors))
        block.up()
        block.goto(j,i)
        block_list.append(block)

block_count = len(block_list)

ball = Ball()


screen.listen()
screen.onkey(game_paddle.move_forward, 'd')
screen.onkey(game_paddle.move_backward, 'a')

game_is_on = True

while block_count > 0:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        ball.refresh()

    if ball.distance(game_paddle) < 50 and ball.ycor() < -240:
        ball.bounce_y()

    for i in block_list:
        if ball.xcor()+10 >= i.xcor()-60 and ball.xcor()-10 <= i.xcor()+60:
            if i.ycor()-20 <= ball.ycor() <= i.ycor()+20:
                ball.bounce_y()
                i.goto(420, 420)
                block_count -= 1


screen.exitonclick()