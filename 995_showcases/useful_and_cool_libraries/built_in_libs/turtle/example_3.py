
import turtle

# Setup
screen = turtle.Screen()
screen.title("Interactive Drawing Tool - Use Arrow Keys!")
screen.bgcolor("lightgray")
screen.setup(width=800, height=600)

# Create drawing turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.pensize(3)
pen.speed(0)

# Variables
pen_down = True
current_color_index = 0
colors = ["blue", "red", "green", "purple", "orange", "black", "pink", "brown"]

# Movement functions
def move_forward():
    pen.forward(20)

def move_backward():
    pen.backward(20)

def turn_left():
    pen.left(15)

def turn_right():
    pen.right(15)

def toggle_pen():
    """Toggle between drawing and moving without drawing"""
    global pen_down
    if pen_down:
        pen.penup()
        pen_down = False
        print("Pen UP - Moving without drawing")
    else:
        pen.pendown()
        pen_down = True
        print("Pen DOWN - Drawing mode")

def change_color():
    """Cycle through available colors"""
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors)
    pen.color(colors[current_color_index])
    print(f"Color changed to: {colors[current_color_index]}")

def clear_screen():
    """Clear all drawings"""
    pen.clear()
    print("Screen cleared!")

def reset_position():
    """Return to center"""
    pen.penup()
    pen.home()
    pen.pendown()
    print("Returned to center")

def increase_size():
    """Increase pen size"""
    current_size = pen.pensize()
    pen.pensize(current_size + 1)
    print(f"Pen size: {current_size + 1}")

def decrease_size():
    """Decrease pen size"""
    current_size = pen.pensize()
    if current_size > 1:
        pen.pensize(current_size - 1)
        print(f"Pen size: {current_size - 1}")

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(toggle_pen, "space")
screen.onkey(change_color, "c")
screen.onkey(clear_screen, "Delete")
screen.onkey(reset_position, "h")
screen.onkey(increase_size, "plus")
screen.onkey(decrease_size, "minus")

# Instructions
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, 250)
instructions.write("Interactive Drawing Tool", align="center", font=("Arial", 16, "bold"))

instructions.goto(0, 220)
instructions.write("Arrow Keys: Move | Space: Pen Up/Down | C: Change Color",
                  align="center", font=("Arial", 10, "normal"))

instructions.goto(0, 200)
instructions.write("H: Home | Delete: Clear | +/-: Pen Size",
                  align="center", font=("Arial", 10, "normal"))

# Console instructions
print("=" * 60)
print("INTERACTIVE DRAWING TOOL")
print("=" * 60)
print("Controls:")
print("  Arrow Keys    - Move and draw")
print("  Space         - Toggle pen (up/down)")
print("  C             - Change color")
print("  H             - Return to home position")
print("  Delete        - Clear screen")
print("  +/-           - Increase/Decrease pen size")
print("=" * 60)
print("\nThis example demonstrates:")
print("- Keyboard event handling")
print("- Interactive user control")
print("- State management (pen up/down, colors)")
print("- Real-time drawing applications")
print("\nReal-world use: Drawing apps, teaching tools, simple game controls")
print("=" * 60)

turtle.done()