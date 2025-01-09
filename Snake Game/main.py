from turtle import Screen,Turtle
from snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food=Food()
scoreBoard=ScoreBoard()
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

    if(snake.snake_head.distance(food)<15):
        food.refresh()
        snake.snake_extention()
        scoreBoard.score_update()

    if(snake.snake_head.xcor()<-285 or snake.snake_head.xcor()>285 or
            snake.snake_head.ycor()<-285 or snake.snake_head.ycor()>285):
                game_start=False
                scoreBoard.game_over()

    for segment in snake.segements[1:]:
        if(snake.snake_head.distance(segment)<10):
            game_start=False
            scoreBoard.game_over()

screen.exitonclick()
