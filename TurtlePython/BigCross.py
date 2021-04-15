from turtle import*
turtle = Turtle()
screen = Screen()

screen.colormode(255)
#Screen Color
R = 0
G = 0
B = 0
#Turtle Color
R1 = 255
G1 = 255
B1 = 255

screen.bgcolor((R, G, B))
turtle.color((R1, G1, B1))

turtle.left(0)
turtle.forward(180)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(180)

#Turtle Color2
R1 = 0
G1 = 255
B1 = 255
turtle.color((R1, G1, B1))

turtle.right(90)
turtle.forward(180)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(180)

#Turtle Color3
R1 = 255
G1 = 0
B1 = 255
turtle.color((R1, G1, B1))

turtle.right(90)
turtle.forward(180)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(180)

#Turtle Color4
R1 = 255
G1 = 255
B1 = 0
turtle.color((R1, G1, B1))
turtle.right(90)
turtle.forward(270)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(270)