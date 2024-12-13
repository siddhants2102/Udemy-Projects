from turtle import Turtle
STARTING_POSITION=[(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE=20
class Snake:
    def __init__(self):

        self.segements = []

        for i in STARTING_POSITION:
            new_segement = Turtle("square")
            new_segement.color("White")
            new_segement.penup()
            new_segement.goto(i)
            self.segements.append(new_segement)

        self.snake_head=self.segements[0]


    def move(self):
        for i in range(len(self.segements) - 1, 0, -1):
            x_pos = self.segements[i - 1].xcor()
            y_pos = self.segements[i - 1].ycor()
            self.segements[i].goto(x_pos, y_pos)

        self.segements[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)


