import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("red")
for i in range(200):
    squary.forward(i)
    squary.left(91)


squary.pencolor("blue")
for i in range(200, 0, -1):
    squary.back(i)
    squary.right(91)
