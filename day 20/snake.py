from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-10,0), (-20,0)]
# this is what called a tuple
MOVE_DISTANCE = 20
UP = 90
DOWN = 270 
LEFT = 180 
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.new_timmy = []
        self.create_snake()
        self.movement()
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)
            
    def add_segment(self, position):
            timmy = Turtle("square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(position)
            self.new_timmy.append(timmy) 
            
    def extend(self):
        self.add_segment(self.new_timmy[-1].position())
    
    def movement(self):
        for onetimmy in range(len(self.new_timmy) - 1, 0, -1):
            new_x = self.new_timmy[onetimmy - 1].xcor()
            new_y = self.new_timmy[onetimmy - 1].ycor()
            self.new_timmy[onetimmy].goto(new_x, new_y)

        self.new_timmy[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.new_timmy[0].heading() != DOWN:
            self.new_timmy[0].setheading(UP)
        
    def down(self):
        if self.new_timmy[0].heading() != UP:
            self.new_timmy[0].setheading(DOWN) 
    
    def left(self):
        if self.new_timmy[0].heading() != RIGHT:
            self.new_timmy[0].setheading(LEFT)
    
    def right(self):
        if self.new_timmy[0].heading() != LEFT:
            self.new_timmy[0].setheading(RIGHT) 