from turtle import Turtle

timmy = Turtle()
timmy.reset()
for step in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
