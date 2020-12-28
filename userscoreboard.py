from turtle import Turtle, Screen

class User(Turtle):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.wins = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def callStatus(self):
        self.goto(-200,-220)
        self.write(self.name, align="center", font=("Courier", 24, "normal"))
        self.goto(200,-220)
        self.write("Computer", align="center", font=("Courier", 24, "normal"))

