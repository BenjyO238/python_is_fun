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

# Draw a square
t.penup()
t.goto(-150, 90)  # Adjusted position up by 40 pixels
t.pendown()
for _ in range(4):
    t.color(random_color())
    t.forward(100)
    t.right(90)

# Draw a circle
t.penup()
t.goto(50, 100)  # Adjusted position
t.pendown()
t.color(random_color())
t.circle(50)

# Draw a triangle
t.penup()
t.goto(-200, -150)  # Adjusted position
t.pendown()
for _ in range(3):
    t.color(random_color())
    t.forward(100)
    t.left(120)

# Draw a trapezoid
t.penup()
t.goto(50, -150)  # Adjusted position
t.pendown()
t.color(random_color())
t.forward(100)     # Bottom side
t.left(120)
t.forward(50)      # Right slant side
t.left(60)
t.forward(100)     # Top side
t.left(60)
t.forward(50)      # Left slant side
t.left(120)

# Keep the window open
screen.mainloop()
