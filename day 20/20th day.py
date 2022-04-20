# SNAKE GAME

from turtle import Screen
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup( width = 600, height = 600 ) 
screen.bgcolor("black")
screen.title("SNAKE GAME") 
screen.tracer(0)
# tracer is a method in screen class which when turned off nothing shows up on the screen.

snake = Snake() 

snake.create_snake() 
food = Food() 
  
scoreboard = Scoreboard()
    

screen.listen()
screen.onkey( snake.up, "Up" )
screen.onkey( snake.down, "Down" )
screen.onkey( snake.left, "Left" )
screen.onkey( snake.right, "Right" )

game_on = True 

while game_on:
    
    screen.update()
    # is a method which displays on the screen what is meant when tracer is turned off.
    time.sleep(0.1)
    snake.movement() 
      
    # detect collision of the snake with food and increase its length
    if snake.new_timmy[0].distance(food) < 15: 
        food.refresh()
        snake.extend()
        scoreboard.increase_score() 
    
    # detect collision with the wall
    if snake.new_timmy[0].xcor() > 280 or snake.new_timmy[0].xcor() < -280 or snake.new_timmy[0].ycor() >280 or snake.new_timmy[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()
        
    # detect collision with its own tail or body. 
    for onetimmy in snake.new_timmy:
        if onetimmy == snake.new_timmy[0]:
            pass
        elif snake.new_timmy[0].distance(onetimmy) < 10:
            game_on = False
            scoreboard.game_over()
            
screen.exitonclick()