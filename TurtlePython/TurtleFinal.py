from turtle import*
import random
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
turtle.speed(10000)

for i in range(360):
     turtle.color((R1, G1, B1))
     R1 = random.randint(0,255)
     G1 = random.randint(0,255)
     B1 = random.randint(0,255)
     turtle.circle(100)
     turtle.forward(500)
     turtle.left(90)
     turtle.forward(20)
     turtle.left(90)
     turtle.forward(500)
     turtle.left(90)
     turtle.forward(20)
     turtle.left(90)
     turtle.left(1)

input("Press any key to exit ...")