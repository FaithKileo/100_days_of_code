STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black") 
        self.penup() 
        self.go_to_start()
        self.setheading(90)
        
    def up(self):
        y_axis = self.ycor() + MOVE_DISTANCE
        self.goto(0 , y_axis) 
        
    def down(self):
        y_axis = self.ycor() - MOVE_DISTANCE
        self.goto(0 , y_axis)  
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
    def is_at_finish_line(self):
        y_axis = self.ycor()
        if y_axis > FINISH_LINE_Y:
            return True
        else: 
            return False
        