from turtle import Turtle, Screen
import random

class Food(Turtle): 
    def __init__(self):
        x = random.randint(-280, 280) # to create an random location of the food on x axis 
        y = random.randint(-280, 280) # to create an random location of the food on y axis
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(x, y)
    

    def refresh(self): # to refresh the location of the food
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)

    

