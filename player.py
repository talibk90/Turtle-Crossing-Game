from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)
        self.ymove = -280
        self.gamespeed = 0.1


    def move(self):
        self.ymove +=MOVE_DISTANCE
        self.goto(0, self.ymove)

    def pos_reset(self):
        self.goto(STARTING_POSITION)
        self.ymove = -280
        

    def is_completed(self):
        if self.ycor() >= FINISH_LINE_Y :
            self.gamespeed *=0.8
            return True
        return False

