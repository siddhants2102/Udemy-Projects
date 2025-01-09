from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=-1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score_update()

    def score_update(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}",align="center",font=("Courier",24,"normal"))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER",align="center",font=("Courier",24,"normal"))