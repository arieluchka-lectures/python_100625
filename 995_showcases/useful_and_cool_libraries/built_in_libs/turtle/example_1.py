
import turtle

# Create a turtle object and screen
screen = turtle.Screen()
screen.title("Turtle Basics - Capabilities Demo")
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()

# 1. MOVEMENT CAPABILITIES
print("Drawing basic shapes to show movement...")
t.pencolor("blue")
t.pensize(2)

# Draw a square (forward and right turns)
for _ in range(4):
    t.forward(100)
    t.right(90)

# 2. PEN CONTROL
# Lift pen to move without drawing
t.penup()
t.goto(150, 0)
t.pendown()

# 3. SHAPE AND COLOR
t.shape("turtle")  # Change shape (arrow, turtle, circle, square, triangle, classic)
t.color("red", "yellow")  # pen color, fill color
t.begin_fill()

# Draw a circle
t.circle(50)
t.end_fill()

# 4. SPEED CONTROL
t.penup()
t.goto(-150, 100)
t.pendown()
t.speed(1)  # Slowest: 1, Fastest: 10, 0 = instant

# Draw a triangle
t.color("green")
for _ in range(3):
    t.forward(80)
    t.left(120)

# 5. MORE ADVANCED MOVEMENT
t.penup()
t.goto(0, -100)
t.pendown()
t.speed(5)

# Draw a star
t.color("purple")
for _ in range(5):
    t.forward(100)
    t.right(144)

# 6. TEXT WRITING
t.penup()
t.goto(-200, -150)
t.pendown()
t.color("black")
t.write("Turtle Graphics!", font=("Arial", 16, "bold"))

# 7. HEADING AND POSITIONING
t.penup()
t.home()  # Return to center (0, 0)
t.setheading(0)  # Face east

# Hide the turtle at the end
# t.hideturtle()

# Keep window open
print("\nTurtle Capabilities Demonstrated:")
print("- Movement (forward, backward)")
print("- Turning (left, right)")
print("- Pen control (up, down, size, color)")
print("- Shapes (turtle, arrow, circle, etc.)")
print("- Filling shapes with colors")
print("- Speed control")
print("- Text writing")
print("- Positioning (goto, home)")

turtle.done()