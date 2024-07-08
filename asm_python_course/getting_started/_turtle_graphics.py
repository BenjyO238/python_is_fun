
'''
Turtle Graphics Commands
forward(distance): Moves the turtle forward by a specified distance.
backward(distance): Moves the turtle backward by a specified distance.
right(angle): Turns the turtle clockwise by a specified angle.
left(angle): Turns the turtle counterclockwise by a specified angle.
penup(): Lifts the pen, so moving the turtle doesn't draw.
pendown(): Lowers the pen to resume drawing.
color(color): Sets the color of the pen.
goto(x, y): Moves the turtle to a specific coordinate.
circle(radius): Draws a circle with the given radius.
'''

import turtle

##################################################
# Create a turtle object- what does this code draw?
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Finish drawing
turtle.done()

##################################################

t = turtle.Turtle()

# Draw a star
for _ in range(5):
    t.forward(100)
    t.right(144)

# Finish drawing
turtle.done()

##################################################
t = turtle.Turtle()

# Draw the square base of the house
for _ in range(4):
    t.forward(100)
    t.right(90)

# Move the turtle to the top of the square
t.right(90)
t.forward(100)
t.left(90)

# Draw the roof
for _ in range(3):
    t.forward(100)
    t.left(120)

# Finish drawing
turtle.done()

##################################################
t = turtle.Turtle()

# Draw a spiral
for i in range(50):
    t.forward(i * 10)
    t.right(144)

# Finish drawing
turtle.done()

##################################################
# Set up a bigger window and trace a star.
screen = turtle.Screen()
screen.setup(400, 400)  # Set the window size to 800x600 pixels

t = turtle.Turtle()

# Move the turtle to the center before drawing
t.penup()
t.goto(-100, -10)  # Adjust this value to move the star up or down
t.pendown()


def mystar(size, filled):
  if filled == True:
    t.begin_fill()
  for x in range(1, 19):
    t.forward(size)
    if x % 2 == 0:
      t.left(175)
    else:
      t.left(225)
  if filled == True:
    t.end_fill()


t.color(0.9, 0.75, 0)
mystar(50, True)
t.color(0, 0, 0)
mystar(50, False)

turtle.done()

