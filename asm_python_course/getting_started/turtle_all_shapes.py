import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(400, 400)  # Set the window size to 400x400 pixels

# Create a turtle object
t = turtle.Turtle()
t.speed(4)  # Set speed to 2 for visibility

# Draw a square
t.penup()
t.goto(-150, 150)  # Move to a starting position
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a star
t.penup()
t.goto(50, 150)  # Move to a new starting position
t.pendown()
for _ in range(5):
    t.forward(100)
    t.right(144)

# Draw the base of the house
t.penup()
t.goto(-150, 0)  # Move to a new starting position
t.pendown()
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

# Draw a spiral
t.penup()
t.goto(100, 0)  # Move to a new starting position
t.pendown()
for i in range(20):
    t.forward(i * 5)  # Adjusted the distance to fit within the window
    t.right(144)

# Draw a filled and unfilled star
t.penup()
t.goto(0, -120)  # Move to a new starting position
t.pendown()

def mystar(size, filled):
    if filled:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled:
        t.end_fill()

t.color(0.9, 0.75, 0)
mystar(30, True)  # Reduced size to fit within the window
t.color(0, 0, 0)
mystar(30, False)  # Reduced size to fit within the window

# Finish drawing
turtle.done()
