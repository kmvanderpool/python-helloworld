import turtle
turtle.bgcolor("white")

squary = turtle.Turtle()
squary.speed(100)
squary.pensize(1)

squary.pencolor("red")
for i in range(200):
    squary.forward(i*2)
    squary.left(91)

squary.pencolor("blue")
for i in range(200, 0, -1):
    squary.forward(i*2)
    squary.left(91)

squary.pencolor("yellow")
for i in range(200):
    squary.forward(i*2)
    squary.left(91)

squary.pencolor("green")
for i in range(200, 0, -1):
    squary.forward(i*2)
    squary.left(91)

squary.pencolor("pink")
for i in range(200):
    squary.forward(i*2)
    squary.left(91)
    

squary.pencolor("orange")
for i in range(200, 0, -1):
    squary.forward(i*2)
    squary.left(91)