import math
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard, Background
from userscoreboard import User


screen = Screen()
screen.tracer(0)

users = []

def game_start():
    screen.tracer(0)
    screen.setup(width=800, height=500)
    screen.bgcolor("black")
    screen.title(titlestring="Pong")

    new_user = User()
    new_user.name = screen.textinput(prompt="What is your Name?", title="Name")
    user_round = screen.numinput(prompt="Best of how many rounds? Pick from\n 1,3,5,10,20", title="Number of rounds")
    new_user.callStatus()
    left_paddle = Paddle()
    right_paddle = Paddle()

    left_paddle.goto(-380, 0)
    right_paddle.goto(360, 0)

    scoreboard = Scoreboard()
    background = Background()
    background.drawline()
    ball = Ball()
    screen.update()

    game_on = True

    while game_on:

        if scoreboard.l_score == math.floor((user_round / 2)) + 1:
            print("User Win")
            new_user.score = [scoreboard.l_score, scoreboard.r_score]
            users.append(new_user)
            new_user.wins += 1
            play_again = screen.textinput(prompt="Play again? - Press Y for yes or N for no", title="Another round?")

            if play_again.lower() == "y" or play_again == "yes":
                scoreboard.r_score = 0
                scoreboard.l_score = 0
                scoreboard.update_scoreboard()

            else:
                screen.clearscreen()
                game_start()

        if scoreboard.r_score == math.floor((user_round / 2)) + 1:
           print("Right Win")
           new_user.score = [scoreboard.l_score, scoreboard.r_score]
           print(new_user.name)
           print(new_user.score)
           users.append(new_user)
           print(users)
           play_again = screen.textinput(prompt="Play again? - Press Y for yes or N for no", title="Another round?")
           if play_again.lower() == "y" or play_again == "yes":
                scoreboard.r_score = 0
                scoreboard.l_score = 0
                scoreboard.update_scoreboard()

           else:
                screen.clearscreen()
                game_start()

        screen.update()
        ball.move()
        screen.update()

        if ball.ycor() > 240 or ball.ycor() < -230:
            ball.bounce()
            screen.update()
        if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -360:
            ball.bounce_x()
            screen.update()


        if ball.xcor() > 380:
            print("You Scored!")
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            ball.reset()
            ball.home()
            ball.bounce_x()
            screen.update()

        if ball.xcor() < -370:
            print("Computer Scored!")
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            ball.reset()
            ball.home()
            ball.bounce_x()
            screen.update()


        screen.listen()
        screen.onkey(left_paddle.up, "Up")
        screen.update()
        screen.onkey(left_paddle.down, "Down")
        screen.update()

        if right_paddle.ycor() < ball.ycor():
            right_paddle.compup()
            screen.update()

        else:
            right_paddle.compdown()
            screen.update()

    screen.exitonclick()

game_start()