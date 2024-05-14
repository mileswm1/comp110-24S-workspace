"""Drawing a basketball court. Go Heels!"""

__author__ = "730323164"


from turtle import Turtle, Screen

def draw_court(turtle: Turtle, x: float, y: float) -> None:
    """Draws the outline of the basketball court."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("saddlebrown")  # Court color
    for _ in range(2):
        turtle.forward(400)  # Court length
        turtle.right(90)
        turtle.forward(200)  # Court width
        turtle.right(90)
    turtle.end_fill()

def draw_hoop(turtle: Turtle, x: float, y: float) -> None:
    """Draws a basketball hoop at specified position."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(15)  # Diameter of hoop

    # Pole
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)

def draw_key(turtle: Turtle, x: float, y: float) -> None:
    """Draws the key area (paint) near the hoop."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("gray")
    for _ in range(2):
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(160)
        turtle.right(90)
    turtle.end_fill()

def draw_center_circle(turtle: Turtle, x: float, y: float) -> None:
    """Draws the center circle of the basketball court."""
    turtle.penup()
    turtle.goto(x, y - 40)  # Adjust y to center the circle
    turtle.pendown()
    turtle.circle(40)

def main() -> None:
    """Main function to draw a basketball court."""
    window = Screen()
    window.bgcolor("light blue")

    nico = Turtle()
    nico.speed(0)

    # Draw the main court
    draw_court(nico, -200, -100)
    # Draw the hoops
    draw_hoop(nico, 180, -85)  # Right hoop
    draw_hoop(nico, -220, -85)  # Left hoop
    # Draw the keys
    draw_key(nico, 160, -60)  # Right key
    draw_key(nico, -240, -60)  # Left key
    # Draw center circle
    draw_center_circle(nico, -20, 0)  # Center of the court

    window.mainloop()

if __name__ == "__main__":
    main()