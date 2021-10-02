from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=8, stretch_wid=1)
        self.penup()
        self.goto(position)

    def move_forward(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def move_backward(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())


