from turtle import Turtle
from colors import Colors
import random 

colors = Colors()

COLOR_LIST = colors.color_list
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = [] 
        
    def create_car(self): 
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid = 1, stretch_len = 2)
        new_car.penup() 
        new_car._color(random.choice(COLOR_LIST)) 
        y_axis = random.randint(-250, 250)
        x_axis = 300
        new_car.goto(x_axis, y_axis)
        self.all_cars.append(new_car) 
        
    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)