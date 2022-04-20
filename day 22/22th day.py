# PONG GAME 
from turtle import Screen, Turtle
from pixels import Paddle 
from ball import Ball
from scoreboard import Scoreboard
import time

# 1st to do (Creating the screen) 
screen = Screen() 

screen.setup( width = 800 , height = 600 )
screen.bgcolor("black") 
screen.title("Pong") 
screen.tracer(0)

r_pixel = Paddle((350, 0)) 
l_pixel = Paddle((-350, 0)) 

ball = Ball()
scores = Scoreboard()

screen.listen()
screen.onkey( fun = r_pixel.up , key = "Up" ) 
screen.onkey( fun = r_pixel.down , key = "Down")

screen.onkey( fun = l_pixel.up , key = "w" ) 
screen.onkey( fun = l_pixel.down , key = "s") 

game_on = True 

while game_on: 
    screen.update() 
    ball.ball_move()
    time.sleep(0.1)
    
# 4th (Creating a ball that continuously keeps on moving both sides) 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()   

# 5th (Detecting collision of the ball with the paddles)
    if ball.distance(r_pixel) < 50 and ball.xcor() > 320: 
        ball.bounce_x()
    
    if ball.distance(l_pixel) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
# 6th (Detect when the paddle misses the ball) 
    if ball.xcor() > 380 :
        ball.reset_position() 
        scores.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scores.r_point() 
        

# 7th (Giving a new score each time the ball goes to the other direction.) 
screen.exitonclick()