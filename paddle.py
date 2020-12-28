from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def up(self):
        if self.ycor() > 180:
            self.backward(10)
        else:
            self.forward(40)

    def down(self):
        if self.ycor() < -170:
            self.forward(10)
        else:
            self.backward(40)

    def compup(self):
        if self.ycor() > 180:
            self.backward(2)
        else:
            self.forward(3)

    def compdown(self):
        if self.ycor() < -170:
            self.forward(2)
        else:
            self.backward(3)

