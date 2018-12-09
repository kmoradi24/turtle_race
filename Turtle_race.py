from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(10):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(98)
  forward(20)
  
ada = Turtle()
ada.color('blue')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('red')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 80)
bob.pendown()

joe = Turtle()
joe.color('yellow')
joe.shape('turtle')

joe.penup()
joe.goto(-160, 60)
joe.pendown()

for turn in range (100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  joe.forward(randint(1,5))