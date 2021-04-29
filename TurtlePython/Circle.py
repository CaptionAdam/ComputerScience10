from turtle import*
turtle = Turtle()
screen = Screen()

turtle.speed(1000)

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
turtle.fillcolor((R1, G1, B1))
turtle.pensize(5)

turtle.begin_fill()
for x in range(360):
  turtle.left(1)
  turtle.forward(1) 
turtle.end_fill()
input("Press any key to exit ...")