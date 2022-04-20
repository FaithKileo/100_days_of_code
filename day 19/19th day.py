from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen() 

# def move_forward():
#     timmy.fd(10)

# screen.listen()
# screen.onkey(fun = move_forward, key = "space")

def ahead():
    timmy.forward(30)
    
def behind():
    timmy.back(30)
    
def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)
    
def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)
    
def clearing():
    timmy.clear()
    # clear() will diretly clear everything but wat z needed is juc clearing the drawing. 
    timmy.penup()
    # clearing and returning the turtle to its original position still leaves the line behind
    # to remove this we need to penup 
    timmy.home()
    timmy.pendown()

screen.listen()

screen.onkey( fun = ahead , key = "w" )
screen.onkey( fun = behind , key = "s" )
screen.onkey( fun = turn_left , key = "a" )
screen.onkey( fun = turn_right , key = "d" )
screen.onkey( fun = clearing , key = "c" )

screen.exitonclick()