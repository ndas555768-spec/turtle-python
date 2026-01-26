import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("violet")

k = 5  # number of petals
scale = 150

for angle in range(360):
    r = scale * math.sin(k * math.radians(angle))
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    t.goto(x, y)

turtle.done()

