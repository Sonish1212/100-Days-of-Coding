from turtle import Turtle


class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=4)
        self.penup()
        self.goto(position)


class Block2(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1.5, stretch_len=4)
        self.penup()
        self.goto(position)


class Block3(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(position)

