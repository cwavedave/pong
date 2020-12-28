from turtle import Turtle

class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,248)
        self.color("white")
        self.hideturtle()
        self.setheading(270)
        self.drawline()


    def drawline(self):
        while self.ycor() > -250:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 180)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(50, 180)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

class Finish(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.color("white")
        self.hideturtle()
        self.write(f"Game Over", align="center", font=("Courier", 24, "bold"))