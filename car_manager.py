from turtle import Turtle
from random import random, choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()


    def reset_cars(self):
        for car in self.car_list:
            car.goto(1000, 1000)
        self.car_list.clear()


    def create(self):
        randomchoice = randint(1, 6)
        if(randomchoice ==1):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            rand_y = randint(-250, 250)
            new_car.goto(300, rand_y)
            self.car_list.append(new_car)
        self.move()


    def move(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)
    


    
        

    




