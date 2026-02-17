import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import winsound
screen = Screen()
screen.setup(width=600, height=600)
cars = CarManager()
score = Scoreboard()

screen.tracer(0)
turtle = Player()

screen.listen()
screen.onkey(turtle.move, "Up")
playing = True

def restart_game():
    global playing
    score.reset_score()
    cars.reset_cars()
    turtle.pos_reset()
    turtle.gamespeed = 0.1
    turtle.clear()
    playing = True

screen.onkey(restart_game, "r")

game_is_on = True
while game_is_on:
    time.sleep(turtle.gamespeed)
    screen.update()
    
    if playing:
        cars.create()

        # Detect collision with car
        for car in cars.car_list:
            if car.distance(turtle) <25:
                winsound.PlaySound(None, winsound.SND_PURGE)
                winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
                turtle.pos_reset()
                score.game_over()
                turtle.write("Press 'R' to Replay", align="center", font=("Courier", 24, "normal"))
                playing = False

        if turtle.is_completed():
            score.update()
            turtle.pos_reset()
        




screen.exitonclick()
