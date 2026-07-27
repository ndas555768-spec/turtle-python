import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Snow White Drawing")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Helper function to draw a filled circle
def circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# -------------------------
# Hair
# -------------------------
circle(0, 100, 100, "black")

# Face
circle(0, 110, 65, "#FFDAB9")

# Hair sides
t.fillcolor("black")
t.penup()
t.goto(-65, 160)
t.pendown()
t.begin_fill()
t.goto(-95, 80)
t.goto(-65, 45)
t.goto(-45, 80)
t.goto(-65, 160)
t.end_fill()

t.penup()
t.goto(65, 160)
t.pendown()
t.begin_fill()
t.goto(95, 80)
t.goto(65, 45)
t.goto(45, 80)
t.goto(65, 160)
t.end_fill()

# -------------------------
# Red Bow
# -------------------------
t.fillcolor("red")

# Left part of bow
t.penup()
t.goto(0, 180)
t.pendown()
t.begin_fill()
t.goto(-65, 220)
t.goto(-90, 185)
t.goto(-45, 160)
t.goto(0, 180)
t.end_fill()

# Right part of bow
t.penup()
t.goto(0, 180)
t.pendown()
t.begin_fill()
t.goto(65, 220)
t.goto(90, 185)
t.goto(45, 160)
t.goto(0, 180)
t.end_fill()

# Bow center
circle(0, 180, 15, "red")

# -------------------------
# Eyes
# -------------------------
circle(-25, 125, 8, "black")
circle(25, 125, 8, "black")

# Eye highlights
circle(-23, 128, 2, "white")
circle(27, 128, 2, "white")

# -------------------------
# Nose
# -------------------------
t.penup()
t.goto(0, 115)
t.pendown()
t.goto(-5, 100)
t.goto(5, 100)

# -------------------------
# Smile
# -------------------------
t.penup()
t.goto(-20, 85)
t.pendown()
t.setheading(-60)
t.circle(25, 120)

# -------------------------
# Neck
# -------------------------
t.penup()
t.goto(-20, 50)
t.pendown()
t.fillcolor("#FFDAB9")
t.begin_fill()
t.goto(-20, 20)
t.goto(20, 20)
t.goto(20, 50)
t.goto(-20, 50)
t.end_fill()

# -------------------------
# Dress
# -------------------------
t.penup()
t.goto(-20, 25)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.goto(-100, -150)
t.goto(100, -150)
t.goto(20, 25)
t.goto(-20, 25)
t.end_fill()

# Yellow collar
t.penup()
t.goto(-20, 25)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.goto(-55, -20)
t.goto(0, 10)
t.goto(55, -20)
t.goto(20, 25)
t.goto(-20, 25)
t.end_fill()

# Red sleeves
t.fillcolor("red")

t.penup()
t.goto(-20, 20)
t.pendown()
t.begin_fill()
t.goto(-70, 0)
t.goto(-110, -70)
t.goto(-80, -90)
t.goto(-20, -30)
t.end_fill()

t.penup()
t.goto(20, 20)
t.pendown()
t.begin_fill()
t.goto(70, 0)
t.goto(110, -70)
t.goto(80, -90)
t.goto(20, -30)
t.end_fill()

# -------------------------
# Hands
# -------------------------
circle(-95, -75, 15, "#FFDAB9")
circle(95, -75, 15, "#FFDAB9")

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()