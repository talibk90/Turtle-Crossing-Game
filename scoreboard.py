from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.goto(0, 250)
        self.write(f"Level: {self.score}", align="center", font=(FONT))


    def reset_score(self):
        self.clear()
        self.score = 1
        self.write(f"Level: {self.score}", align="center", font=(FONT))
        

    def update(self):
        self.clear()
        self.score +=1
        self.write(f"Level: {self.score}", align="center", font=(FONT))