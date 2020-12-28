from turtle import Turtle
import random

start = random.randint(100,180)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(start)
        self.x_move = 1.5
        self.y_move = 1.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.faster()

    def stop(self):
        self.x_move = 0
        self.y_move = 0

    def faster(self):
        self.y_move *= 1.1
        self.x_move *= 1.1

    def reset(self):
        self.x_move = 1.5
        self.y_move = 1.5