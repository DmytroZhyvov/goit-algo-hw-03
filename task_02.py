import turtle


def koch_curve(t, order, size):
    """Draw koch curve"""

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    """Draw koch snowflake"""

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Enter recursion level: "))
        draw_koch_snowflake(level)
    except ValueError:
        print("Invalid input.")
