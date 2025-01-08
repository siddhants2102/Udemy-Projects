from turtle import Screen
from snake import Snake
from Food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food=Food()
#EVENT LISTNERS
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_start = True
while game_start:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if(snake.snake_head.distance(food)<10):
        food.refresh()

screen.exitonclick()
