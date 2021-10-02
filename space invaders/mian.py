import math
import turtle
from turtle import Turtle, Screen
import random
import winsound


screen = Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.bgpic("space_invaders_background.gif")

turtle.register_shape('player.gif')
turtle.register_shape('invader.gif')

# setting up the border
border_pen = Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.color('white')
border_pen.setposition(-300, 300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()

# setting up the score
score = 0
scoreboard = Turtle()
scoreboard.speed(0)
scoreboard.color('cyan')
scoreboard.penup()
scoreboard.setposition(-290, 270)
score_string = f"Score: {score}"
scoreboard.write(score_string, font=("Courier", 14, "normal"), align='left')
scoreboard.hideturtle()

# setting the player
player = Turtle()
player.shape('player.gif')
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15
enemyspeed = 2
no_of_enemies = 15
enemy_list = []

# setting the enemy
for i in range(no_of_enemies):
    enemy_list.append(Turtle())
for enemy in enemy_list:
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# setting the bullet
bullet = Turtle()
bullet.shape('triangle')
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 70

bullet_state = 'ready'


def move_left():
    x = player.xcor() - playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor() + playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bullet_state
    if bullet_state == 'ready':
        winsound.PlaySound('Space Invaders_laser.wav', winsound.SND_ASYNC)
        bullet_state = 'fire'
        x = player.xcor()
        y = player.ycor() + 20
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# on keyboard
turtle.listen()
turtle.onkey(move_right, 'd')
turtle.onkey(move_left, 'a')
turtle.onkey(fire_bullet, 'space')

while True:
    for enemy in enemy_list:
        x = enemy.xcor() + enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemy_list:
                y = e.ycor() - 30
                e.sety(y)
            enemyspeed *= -1

        # collision between enemy and bullet
        if is_collision(enemy, bullet):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bullet_state = 'ready'
            bullet.setposition(0, -340)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
           # update the score
            score += 10
            score_string = f"Score: {score}"
            scoreboard.clear()
            scoreboard.write(score_string, font=("Courier", 14, "normal"), align='left')

        # collision between enemy and player
        if is_collision(enemy, player):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            game_over = Turtle()
            game_over.write("Game Over", font=("Courier", 20, "bold"))
            game_over.setposition(0, -250)
            break

    # move the bullet
    if bullet_state == 'fire':
        y = bullet.ycor() + bulletspeed
        bullet.sety(y)

    # check if the bullet has cross the screen
    if bullet.ycor() > 270:
        bullet.hideturtle()
        bullet_state = 'ready'

while True:
    wn.update()