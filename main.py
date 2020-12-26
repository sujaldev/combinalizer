import turtle


window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)


def split_paths(splits, length=100):
    for i in range(1, splits+2):
        for k in range(1, splits):
            pen.left(360/splits*i)
            pen.forward(length)
            pen.left(-45+(90/(splits-1)*k))
            pen.forward(length/2)
            pen.penup()
            pen.home()
            pen.pendown()


def make(n, r=1, length=100):
    for i in range(1, n+2):
        pen.right(360/n*i)
        pen.forward(length)
        pen.home()
    split_paths(n, length)


split_paths(2)
turtle.done()
