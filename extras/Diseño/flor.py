from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 0.9, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(90)
    circle(40, 24)

bgcolor("white")
title("Mi Dibujo con Turtle")

for _ in range(4):
    forward(100)
    right(90)

exitonclick()
