from turtle import Screen
import time
from snake import Snake
from Food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("Welcome to the snake game!")
screen.tracer(0) # to do with animation have to look it up in detail. 

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True # to use it in while loop 
while game_is_on:
    screen.update() # to do with animation have to loop it up 
    time.sleep(0.1) # to slow down the time by 0.1 seconds to make snake move smoothly. 
    snake.move()
    if snake.head.distance(food) < 15: #detect collision with food
        scoreboard.increase_score() # got this function from scoreboard file to manage scores. 
        snake.extend() # got this function from snake file to extend the snake if collision with food detected.
        food.refresh() # to create new food object if collision is detected. 
    if snake.head.xcor() > 470 or snake.head.xcor() < -470 or snake.head.ycor() > 400 or snake.head.ycor() < -400: # to limit the boundary of the snake within the pixel range. 
        game_is_on = False # to break the loop if snakes tries to go out of the pixels range. 
        scoreboard.game_over() # imported from scoreboard file to display game over. 
    for segment in snake.segments[1:]: # check all the segments of the snake ignoing the 1st one. 
        if snake.head.distance(segment) < 10: # to check the distance of head segment from the other segments. 
            game_is_on = False # to break the loop if 1st segment detected near within the pixel range 10. 
            scoreboard.game_over()
        
    

screen.exitonclick()














