import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("black")

# Create and configure the turtle
t = turtle.Turtle()
t.speed(2)
t.hideturtle()

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Draw the base of the house
t.penup()
t.goto(-100, -100)  # Lowered position to center the house more
t.pendown()
for _ in range(4):
    t.color(random_color())
    t.forward(200)
    t.left(90)

# Draw the roof
t.penup()
t.goto(-100, 100)
t.pendown()
t.color(random_color())
t.goto(0, 200)
t.goto(100, 100)

# Draw the door
t.penup()
t.goto(-30, -100)
t.pendown()
for _ in range(2):
    t.color(random_color())
    t.forward(60)
    t.left(90)
    t.forward(100)
    t.left(90)

# Draw the first window
t.penup()
t.goto(40, 0)
t.pendown()
for _ in range(4):
    t.color(random_color())
    t.forward(40)
    t.left(90)

# Draw the second window
t.penup()
t.goto(-80, 0)
t.pendown()
for _ in range(4):
    t.color(random_color())
    t.forward(40)
    t.left(90)

# Keep the window open
screen.mainloop()
