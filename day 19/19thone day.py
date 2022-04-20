# TURTLE RACING GAME

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen() 
screen.setup( width = 500, height = 400 )
user_bet = screen.textinput( title = "MAKE YOUR BET", prompt = "Which turtle will win? Choose the color: ")
y_axis = [ -70, -40, -10, 20, 50, 80 ]
all_turtles = []


for turtle_index in range(0, 5):
    
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.penup()
    timmy.color("blue")
    timmy.goto( x = -230 , y = y_axis[turtle_index] )
    all_turtles.append(timmy)
    
if user_bet:
    is_race_on = True 
    
while is_race_on:
    
    for turtle in all_turtles:
        turtle_speed = random.randint(0, 10)
        turtle.forward(turtle_speed)
    

screen.exitonclick()