from turtle import Turtle, Screen 
import random

timmy = Turtle()
timmy.shape("turtle")

# colours = ["red", "blue", "orange", "black", "pink", "yellow"]

# def numbers(num_sides):    
#     angle = 360/num_sides

#     for _ in range(num_sides): 
        
#         timmy.right(angle) 
#         timmy.forward(100) 
    
# for number in range(3, 11):
    
#     timmy._color(random.choice(colours))
#     # the colors do not appear because the list of colors is not recognised.
#     print(numbers(number))


# for _ in range(15):
#     timmy.forward(10) 
#     timmy.penup() 
#     timmy.forward(10) 
#     timmy.pendown()


# # timmy.colormode(255)

# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# angles = [ 0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed("fastest")

# for _ in range(100):
#     # timmy.color(rand_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(angles))
 

for _ in range(100):
    timmy.color("blue")
    timmy.circle(100)
    timmy.setheading( timmy.heading() + 10 )
    timmy.color("red")


screen = Screen() 
screen.exitonclick()