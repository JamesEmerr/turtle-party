# J programming
# turtle party
# 08.05.23

import turtle
turtle.color("red")

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

for n in range(3, 10):
  move(50)
  polygon(n, 100 / n)
  back(50)
  turtle.right(360 / 7)
