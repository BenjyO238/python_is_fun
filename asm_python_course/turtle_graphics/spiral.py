import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("black")

# Create and configure the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Draw the spiral
for i in range(100):
    t.color(random_color())
    t.forward(i * 2)
    t.right(45)

# Keep the window open
screen.mainloop()
