from turtle import exitonclick
from turtle import forward, left, goto, penup, pendown
from math import sqrt
from random import randint

def draw_street():
    penup()
    goto (-300, 0)
    pendown()
    #b = 0
    a = 0

    for x in range(10):
        while True:
            p = randint(30, 80)
            if abs(p - a) > 10:
                a = p
                break
        #space_houses(a, b)
        draw_house(a)

def draw_house(a):
    c = round(sqrt(2) * a)

    # obvodove steny
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)

    # pricka ve stene
    left(90+45)
    forward(c)
    left(90)

    # strecha - TODO komin
    forward(c/2)
    left(90)
    forward(c/2)
    left(90)

    # druha pricka ve stene
    forward(c)
    left(45)

#def space_houses(a, b):
 #   forward(a * b /100)
  #  b = a

draw_street()
exitonclick()
