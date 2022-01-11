import turtle

def main():
    # Create a turtle object
    screen = turtle.Screen()
    screen.colormode(255)
    michaelangelo = turtle.Turtle()
    michaelangelo.speed(0)
    michaelangelo.color((140, 50, 50))

    # Ask the turtle to move around the canvas
    for i in range(1000):
        michaelangelo.forward(50 + i)
        michaelangelo.right(93)
        michaelangelo.color((
                (150 + i) % 255,
                (50 + i) % 255,
                (50 + i) % 255,
        ))

    turtle.exitonclick()


if __name__ == "__main__":
    main()

