# Eric Chen
# CompSci 111 Project 2 Part 2

from visual import *
from math import sqrt

def fractal(n, l= 1):

    odd = False

    for i in range(0, n+1):
# Draw straight triangle
        if odd:
            t = paths.triangle(length=l*(sqrt(3)/3)**i)
            t2 = paths.triangle(length=-l*(sqrt(3)/3)**i)
            curve(pos=t.pos)
            curve(pos=t2.pos)
            odd = False
# Draw rotated triangle
        else:
            t = paths.triangle(length=l*(sqrt(3)/3)**i, rotate=pi/6)
            t2 = paths.triangle(length=-l*(sqrt(3)/3)**i, rotate=pi/6)
            curve(pos=t.pos)
            curve(pos=t2.pos)
            odd = True

fractal(10)