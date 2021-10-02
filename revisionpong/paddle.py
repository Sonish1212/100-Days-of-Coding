from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.color('white')
        self.penup()

    def move_forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_backward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


