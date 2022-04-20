from turtle import Turtle

class Paddle(Turtle): 
    
    def __init__(self, position):
        super().__init__()

        # 2nd (creating two randomly moving wall like object) 
        # timmy = Turtle() 

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position) 
           
    #  3rd (moving the pixels) 

    def up(self): 
        x_axis = self.xcor() 
        y_axis = self.ycor() + 20 
        self.goto(x = x_axis, y = y_axis) 
        
    def down(self): 
        x_axis = self.xcor() 
        y_axis = self.ycor() - 20 
        self.goto(x = x_axis, y = y_axis)
    