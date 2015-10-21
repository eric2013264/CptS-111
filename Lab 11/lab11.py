# By Eric Chen
# Nov 20 2013
# Lab 11
# Python 2.7 / VPython 6.0.0

from visual import *
from random import *

display(height = 700, width = 1000)
###############################################################################################################
#GENERAL
center = (0,0,0)

###############################################################################################################
#TRUNK
trunk_axis_x = 0
trunk_axis_y = 0
trunk_axis_z = 0
trunk_axis_position = (trunk_axis_x, trunk_axis_y, trunk_axis_z)
trunk_position = center
trunk_x = 0
trunk_y = 0
trunk_z = 0
trunk_position = (trunk_x, trunk_y, trunk_z)
trunk_radius = 0 	# tree trunk radius

###############################################################################################################
#LEAVES
leaves_radius = 0 	# leaves radius

###############################################################################################################
#GROUND
ground_size = (400,1,400)

###############################################################################################################

ground = box(pos = center, size = ground_size, color = (0.8,0.3,0.3))

origin = sphere(pos = (0,0,0), radius = 2, color = color.blue)



for i in range(0,100):
	trunk_x = randint(-200,200)
	trunk_z = randint(-200,200)
	trunk_axis_y = randint(20,150)
	trunk = cylinder(pos = (trunk_x, 0, trunk_z), axis = (0,trunk_axis_y,0), radius = trunk_radius, material = materials.wood)
	
	if trunk_axis_y > 70:
		leaves_radius = randint(6,11)
		trunk_radius = randint(3,4)
	else:
		leaves_radius = randint(3,6)
		trunk_radius = 2

	leaves = sphere(pos = (trunk_x, trunk_axis_y, trunk_z), radius = leaves_radius, color = color.green)

###############################################################################################################
	root = (200 - random() * 400,0,200 - random() * 400)
	l1 = [curve(pos=[root, (root[0] + 3 - random() * 6, 10, root[2] + 3 - random() * 6)], color=(0,1,0)),
			  curve(pos=[root, (root[0] + 3 - random() * 6, 10, root[2] + 3 - random() * 6)], color=(0,1,0))]

	levels = [l1]
	for i in range(1,10):
		levels.append([])

	for i in range(1,int(5 + random() * 5)):
		current_level = levels[i]
		prev_level = levels[i - 1]
		for c_curve in prev_level:
			#Make up to two new branches
			endpoint = c_curve.pos[1]
			if random() < 0.8:
				current_level.append(curve(pos=[endpoint, endpoint + (4 - random() * 8,  random() * 4, 4 - random() * 8)], color=(0,1,0)))
			if random() < 0.8:
				current_level.append(curve(pos=[endpoint, endpoint + (4 - random() * 8, random() * 4, 4 - random() * 8)], color=(0,1,0)))






