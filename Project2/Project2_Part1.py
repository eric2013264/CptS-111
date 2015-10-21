# Eric Chen
# CompSci 111 Project 2 Part 1

from visual import *
from sys import exit

display(height=700, width=700)

n=3

def subdivide(n=0, L=100, value=(0,0,0)):
	(x,y,z) = (value)
# Corner Coordinates
	a = (x+L, y-L, z+L)
	b = (x+L, y-L, z-L)
	c = (x-L, y-L, z+L)
	d = (x-L, y-L, z-L)
# Draw Pyramid
	curve(pos=[(x,y,z),(a)])
	curve(pos=[(x,y,z),(b)])
	curve(pos=[(x,y,z),(c)])
	curve(pos=[(x,y,z),(d)])
	curve(pos=[(a),(c)])
	curve(pos=[(b),(d)])
	curve(pos=[(a),(b)])
	curve(pos=[(c),(d)])
	if n > 0:
		subdivide(n-1, L/2, (x,y,z))
		subdivide(n-1, L/2, ((x+L/2), (y-L/2), (z+L/2)))
		subdivide(n-1, L/2, ((x+L/2), (y-L/2), (z-L/2)))
		subdivide(n-1, L/2, ((x-L/2), (y-L/2), (z+L/2)))
		subdivide(n-1, L/2, ((x-L/2), (y-L/2), (z-L/2)))
		
subdivide(n)


