import turtle

def hilbert_curve(turtle, order, size, angle):
    if order == 0:
        return
    turtle.forward(size)
    turtle.left(angle)
    hilbert_curve(turtle, order-1, size, -angle)
    turtle.forward(size)
    turtle.right(angle)
    hilbert_curve(turtle, order-1, size, angle)
    turtle.forward(size)
    hilbert_curve(turtle, order-1, size, angle)
    turtle.right(angle)
    turtle.forward(size)
    hilbert_curve(turtle, order-1, size, -angle)
    turtle.left(angle)
    turtle.forward(size)

window = turtle.Screen()
window.title("Hilbert Curve")
hilbert_turtle = turtle.Turtle()
hilbert_turtle.speed(2)

hilbert_curve(hilbert_turtle, 4, 20, 90)

window.mainloop()
