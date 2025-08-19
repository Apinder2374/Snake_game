from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Aerial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white") 
        self.penup()
        self.goto(0,370)
        self.write(f"Score = {self.score} ",False, ALIGNMENT, FONT) # score starts from 0
        self.hideturtle()

    def increase_score(self):
        self.score += 1 # to increase the score.
        self.clear() # to clear the score if there is an increment
        self.write(f"Score = {self.score} ",False, ALIGNMENT, FONT) # to update heading.
    
    def game_over(self): # to display the GAME OVER!
        self.goto(0,0) 
        self.write(f"GAME OVER. ",False, ALIGNMENT, FONT)

