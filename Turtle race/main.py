from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("AliceBlue")


user_bet = screen.textinput("CHOOSE YOUR BET", "Which turtle will win the race?\n(violet,blue,green,yellow,"
                                               "orange,red):").lower()
colour = ["violet", "blue", "green", "yellow", "orange", "red"]
turtles = []


if user_bet in colour:
    race_on = True
    screen.tracer(0)
    start_turtle = Turtle()
    end_turtle = Turtle()

    start_turtle.hideturtle()
    end_turtle.hideturtle()

    start_turtle.penup()
    end_turtle.penup()

    start_turtle.goto(x=-228, y=-190)
    end_turtle.goto(x=237, y=-190)

    start_turtle.pendown()
    start_turtle.pensize(5)
    end_turtle.pendown()
    end_turtle.pensize(5)

    start_turtle.setheading(90)
    end_turtle.setheading(90)

    start_turtle.color("LightSeaGreen")
    end_turtle.color("LightSeaGreen")

    start_turtle.forward(400)
    end_turtle.forward(400)

    for i in range(0, 6):
        new_turtle = Turtle("turtle")
        new_turtle.color(colour[i])
        new_turtle.penup()
        new_turtle.goto(x=-240, y=(-70 + (i * 40)))
        turtles.append(new_turtle)

    screen.update()
    screen.tracer(1)

else:
    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.write("WRONG INPUT", align="center")


while race_on:

    for turtle_object in turtles:
        if turtle_object.xcor() >= 240:
            race_on = False
            if turtle_object.pencolor() == user_bet:
                print(f"You Won the bet.The {turtle_object.pencolor()} turtle won the race.")
                break
            else:
                print(f"You loss the bet.The {turtle_object.pencolor()} turtle won the race.")
                break
        speed = random.randint(0, 10)
        turtle_object.forward(speed)

screen.exitonclick()
