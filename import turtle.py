import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

n = 360
h = 0

for i in range(n):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.circle(150)
    t.right(1)
    h += 1/n

turtle.done()
