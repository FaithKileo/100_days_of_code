from turtle import Turtle

FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.high_score = 0 
        self.score = 0 
        self.color("white") 
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align= "center", font = FONT)
        self.hideturtle() 
        
    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align= "center", font = FONT)
        
    # # keeping track of the highest score
    # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score == self.score 
    #     self.score = 0 
    #     self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font = FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()