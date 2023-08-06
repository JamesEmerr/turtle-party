# J programming
# turtle party

import turtle
from turtle import *
shape('turtle')
turtle.color("red")
turtle.speed(10)
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
def move(len):
    back(-1 * len)
def polygon(num, size):
  for j in range(num): 
    turtle.forward(size)
    turtle.left(360/ num)
for n in range(20, 32):
  move(50)
  polygon(n, 100 / n)
  back(20)
  turtle.right(360 / 12)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
color('yellow')
turtle.stamp()
color('red')
turtle.right(180)
turtle.forward(125)
turtle.right(180)
