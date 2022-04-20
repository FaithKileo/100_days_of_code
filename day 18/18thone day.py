# import colorgram
# colors = colorgram.extract('day 18\image.jpg', 30)

# rbg_colors = []
# for color in colors:
    
#     r = color.rgb.r 
#     g = color.rgb.g 
#     b = color.rgb.b 
    
#     rbg_colors.append((r, g, b))
             
# print(rbg_colors)

import turtle as turtle_module
import random

timmy = turtle_module.Turtle()
screen = turtle_module.Screen()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
turtle_module.colormode(255)

color_list = [(235, 239, 252), (40, 7, 178), (87, 248, 180), (219, 156, 111), (146, 6, 81), (239, 45, 119), (11, 211, 85), (12, 139, 60), (215, 115, 177), (111, 104, 234), (249, 249, 60), (55, 232, 70), (184, 179, 246), (210, 103, 11), (40, 35, 246), (159, 124, 235), (241, 45, 37), (29, 121, 144), (190, 41, 106), (138, 8, 5), (82, 247, 253), (21, 6, 101), (10, 209, 218), (94, 9, 57), (227, 166, 202), (213, 121, 28), (10, 110, 49)]

timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    color = random.choice(color_list)
    timmy.dot(20, color)
    timmy.fd(50)
    
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()
