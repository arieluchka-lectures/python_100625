import turtle
import random

# Setup
screen = turtle.Screen()
screen.title("Colorful Spiral Pattern Generator")
screen.bgcolor("black")

# Create turtle
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed
artist.width(2)

# Color palette
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "white"]

# Draw spiral pattern
print("Generating spiral pattern...")

# Variables for the spiral
distance = 10
angle = 45
increment = 2

# Create the spiral
for i in range(200):
    # Change color randomly or in sequence
    artist.pencolor(colors[i % len(colors)])

    # Draw and move
    artist.forward(distance)
    artist.right(angle)

    # Increase distance gradually for spiral effect
    distance += increment

# Position for signature
artist.penup()
artist.goto(0, -280)
artist.pencolor("white")
artist.write("Spiral Art Generator", align="center", font=("Courier", 14, "normal"))

print("Spiral pattern complete!")
print("\nThis example demonstrates:")
print("- Using loops for repetitive patterns")
print("- Color cycling for visual appeal")
print("- Mathematical patterns (spirals)")
print("- Fast rendering with speed(0)")
print("\nReal-world use: Digital art, pattern generation, decorative graphics")

turtle.done()