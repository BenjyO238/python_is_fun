import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(400, 400)  # Set the window size to 400x400 pixels

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create and configure the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()


# Function to generate a random color
def random_color():
  return (random.random(), random.random(), random.random())


# Main drawing function
def draw_star_shape(size, points):
  angle = 360 / points
  for _ in range(points):
    t.color(random_color())
    t.forward(size)
    t.right(angle)

    # Draw inner lines
    inner_size = size / 2
    t.forward(inner_size)
    t.left(angle * 2)
    t.forward(inner_size)
    t.right(angle * 2)


# Function to draw a spiral
def draw_spiral(size, turns):
  for i in range(turns):
    t.color(random_color())
    t.forward(i * size / turns)
    t.right(30)


# Main drawing
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the main star shape
draw_star_shape(300, 12)

# Draw spirals at the points of the star
for _ in range(12):
  t.penup()
  t.forward(300)
  t.pendown()
  draw_spiral(50, 20)
  t.penup()
  t.backward(300)
  t.right(30)

# Draw a central pattern
t.penup()
t.goto(0, 0)
t.pendown()
for _ in range(36):
  t.color(random_color())
  t.forward(100)
  t.backward(100)
  t.right(10)

# Keep the window open
screen.mainloop()
