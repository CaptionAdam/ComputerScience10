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

for x in range(360):
  turtle.left(1)
  turtle.forward(1) 