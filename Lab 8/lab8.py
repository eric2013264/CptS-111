import turtle as t
t.forward(100)
t.backward(200)
t.shape("turtle")
t.hideturtle() 
t.fd(100) # same thing as forward
t.left(90) # turn left 90 degrees
t.right(90) # turn right 90 degrees

# drawing a line away from previous point
t.penup() # "pen" leaves paper
t.setposition(100, -100) # position to return to
t.pendown()
t.fd(130)

t.clear # to clear the image
t.reset() # resets turtle


def square(length): # a function that draws a square using a for-loop
	for in in range(4):
		t.fd(length)
		t.left(90)
square(60)
square(100)
square(200)

t.reset() # drawing circles
t.circle(100)
t.circle(-50)

t.reset() # speeds up 
t.speed(0)
t.circle(100)
t.circle(-50)

t.color("blue") # changes cursor color

t.pensize(100) # changes thickness
t.fd(100)

# really cool color for loop 
colors = ["blue", "green", "purple", "cyan", "magenta", "violet"] 
t.reset()
t.tracer(0, 0)
for i in range(45):
	t.color(colors[i % 6])
	t.pendown()
	t.fd(2 + i * 5)
	t.left(45)
	t.width(i)
	t.penup()

# cool geometric shape
t.reset()
>>> t.color("red")
>>> for angle in range(0, 360, 15):
...     t.seth(angle)
...     t.circle(100)
	
	t.update()


# actual lab 8

import turtle as t

def into_position(t):
	t.penup()
	t.setposition(-200,-200)
	t.pendown()
	t.left(90)

into_position(t)

i = 0
length = 400
while i < 20:
	t.fd(length)
	t.right(90)
	t.fd(length)
	t.right(90)
	length = length - 20
	i = i + 1

# drawing a lot of circles, one bigger than the last
i = 0
y_coordinate = -5
circle_size = 5
while i < 100:
	t.circle(circle_size)
	t.penup()
	t.setposition(0,y_coordinate)
	t.pendown()
	circle_size += 5
	y_coordinate -= 5
	i += 1

# point identifier
def printxy(x, y):
	print(x, y)
t.onscreenclick(printxy)
t.mainloop()
