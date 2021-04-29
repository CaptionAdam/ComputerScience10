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
turtle.pensize(5)

turtle.circle(100)
turtle.pu()
turtle.goto(65, 175)
turtle.pd()
turtle.left(45)
turtle.forward(80)

for x in range(90):
     turtle.left(2)
     turtle.forward(1)

turtle.forward(100)

turtle.pu()
turtle.goto(-65, 175)
turtle.pd()
turtle.left(-90)
turtle.forward(80)

for x in range(90):
     turtle.right(2)
     turtle.forward(1)

turtle.forward(100)
turtle.pu()
turtle.goto(0, 40)
turtle.left(45)
turtle.pd()
turtle.circle(20)

turtle.pu()
turtle.goto(30, 120)
turtle.pd()
turtle.circle(20)
turtle.circle(10)

turtle.pu()
turtle.goto(-30, 120)
turtle.pd()
turtle.circle(20)
turtle.circle(10)

input("Press any key to exit ...")