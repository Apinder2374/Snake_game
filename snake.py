from turtle import Turtle
# squares = snakes

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)] # starting position of the 1st, 2nd and 3rd snake.
MOVE_DISTANCE = 20 
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = [] # to add the 3 segments of the snake
        self.create_snake()
        self.head = self.segments[0] # to hold the 1st segment of the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:  # to create multiple squares to form a snake 20*20 dimension. 
            self.add_segment(position)

    def add_segment(self,position):
        tim = Turtle() # using class 
        tim.color("white")
        tim.shape("square")
        tim.penup() 
        tim.goto(position) # going to the (x,y) postions from the STARTING_POSITIONS list above. 
        self.segments.append(tim) #append it to new list so that we can get our snake in list to make it move forward. 
    
    def extend(self):
        self.add_segment(self.segments[-1].position()) # to extend the snake if collision has been with food

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # x cordinates for 2nd square 
            new_y = self.segments[seg_num - 1].ycor() # y cordinates for 2nd square 
            self.segments[seg_num].goto(new_x, new_y) # using (x,y) cordinates of 2nd square to move 3rd square to the 2nd position to make smooth turns
        self.head.forward(MOVE_DISTANCE) # making the snake move forward
        # self.head.left(90) # making the snake turn left at 90 degrees. 
    
    def up(self):
        if self.head.heading() != DOWN: # if snake is going up it cant go down 
            self.head.setheading(UP) 
        
    def down(self):
        if self.head.heading() != UP: # if snake is going down it cant go up
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT: # if snake is going left it cant go right 
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT: # if snake is going right it cant go left
            self.head.setheading(RIGHT)
        

