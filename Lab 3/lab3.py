# python3
# written by Eric Chen -- Sept 10, 2013
# Pizza Deal Caluculator v0.1
from math import *

pizza_count = 0
best_deal = 100
pizza_number = 0

while True:

	pizza_number = pizza_number + 1
	pizza_shape = input("what is the shape of your pizza?: ")
	pizza_diameter = float(input("what is the diameter of your pizza?: "))
	if pizza_shape == "oval":
		pizza_diameter_2 = float(input("what is the other diameter of your pizza?: "))
		pizza_price = float(input("what is the price of your pizza?: "))
	else:
		pizza_price = float(input("what is the price of your pizza?: "))

	if pizza_shape == "round":
		area = pi*((pizza_diameter/2)**2)
		print("pizza area is", round(area,2), "square inches")
	if pizza_shape == "oval":
		area = (pi*pizza_diameter*pizza_diameter_2)/4
		print("pizza area is", round(area,2), "square inches")
	if pizza_shape == "square":
		area = (pizza_diameter**2)
		print("pizza area is", round(area,2), "square inches")

	cost_per_square_inch = pizza_price / area #cost_per_square_inch loop begins
	if cost_per_square_inch < best_deal:
		best_deal = cost_per_square_inch
		pizza_count = pizza_number

		if pizza_shape == "round":
			dimention = (pizza_diameter)
			shape = "round"
		if pizza_shape == "oval":
			dimention = (pizza_diameter, pizza_diameter_2)
			shape = "oval"
		if pizza_shape == "square":
			dimention = (pizza_diameter, pizza_diameter)
			shape = "square"

	print("the cost per square inch is $", round(cost_per_square_inch,3))

	again = str(input("Enter Another? (y/n): "))
	if again == "n":
		print("The best deal is pizza number", pizza_count ,", the", shape ,"pizza, measuring", dimention)
		break

#python3 lab3.py
