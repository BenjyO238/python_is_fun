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

# Draw the star
t.penup()
t.goto(-100, 60)  # Adjusted position to move up and left
t.pendown()
for _ in range(5):
    t.color(random_color())
    t.forward(200)
    t.right(144)

# Keep the window open
screen.mainloop()
