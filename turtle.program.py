# turtle
# Anders B
# 10.27.17

from turtle import*
from random import randint
import ctypes
import time


while True:
    ctypes.windll.user32.MessageBoxW(0, "R for red, g for green, y for yellow, b for blue. Space bar to pick the pen up and again to put the pen back down. S to draw a star, o to draw an octogon, and h to draw a hexagon. Finally, click on the screen to clear all drawings.", "Commands", 1)
    time.sleep(1.5)
    break

def red():
    color("red")
def green():
    color("green")
def blue():
    color("blue")
def yellow():
    color("yellow")

def pen():
    if isdown():
        penup()
    else:
        pendown()
def wipe(x, y):
    clear()

def up_arrow():
    forward(50)

def left_arrow():
    left(45)

def right_arrow():
    right(45)

def down_arrow():
    back(50)

def draw_star():
    points, deg = find_deg()
    for i in range(points):
        forward(100)
        left(deg)
def find_deg():
    ps = randint(9,36)
    ds = (180 - (360/int(ps)))
    return ps,ds
def draw_octogon():
    for i in range(8):
        up_arrow()
        right_arrow()
def draw_hexagon():
    for i in range(2):
        up_arrow()
        right_arrow()
        up_arrow()
        right_arrow()
        right_arrow()
        up_arrow()
        right_arrow()
onkeypress(red, "r")
onkeypress(green, "g")
onkeypress(blue, "b")
onkeypress(yellow, "y")
onkeypress(pen, "space")
onkeypress(up_arrow, "Up")
onkeypress(left_arrow, "Left")
onkeypress(right_arrow, "Right")
onkeypress(down_arrow, "Down")
onkeypress(draw_star, "s")
onkeypress(draw_octogon, "o")
onkeypress(draw_hexagon, "h")
onscreenclick(wipe)
listen()
