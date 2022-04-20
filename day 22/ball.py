from turtle import Turtle 

class Ball(Turtle): 
    
    def __init__(self):
        super().__init__()
        self.shape("circle") 
        self.color("white")
        self.goto(x = 0, y = 0) 
        self.penup() 
        self.x_move = 10 
        self.y_move = 10 
        self.ball_speed = 0.1
        # above is to increase the speed of the ball everytime it hits the paddle 
        # so as to make the game more exciting and remove the boredom.
        
    def ball_move(self):
        x_axis = self.xcor() + self.x_move 
        y_axis = self.ycor() + self.y_move 
        self.goto(x = x_axis, y = y_axis) 
        
    def bounce_y(self):
        self.y_move *= -1 
        
    def bounce_x(self):
        self.x_move *= -1 
        self.ball_speed *= 0.9
        # above is to increase the speed of the ball everytime it hits the paddle 
        # so as to make the game more exciting and remove the boredom.
        
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1 
        # above is to increase the speed of the ball everytime it hits the paddle 
        # so as to make the game more exciting and remove the boredom.
        self.bounce_x()