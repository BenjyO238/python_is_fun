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

# Draw the flower petals
for _ in range(36):
    t.color(random_color())
    t.circle(50)
    t.right(10)

# Draw the stem
t.penup()
t.goto(0, -50)
t.pendown()
t.color(random_color())
t.right(90)
t.forward(100)

# Draw the leaves
for _ in range(2):
    t.color(random_color())
    t.circle(30, 180)
    t.right(180)

# Keep the window open
screen.mainloop()
