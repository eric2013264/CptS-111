class Position:
	def __init__(self, x, y):
		# takes parameters self, x, and y, and sets the initial postion 
		# (self.x and self.y are set to x and y)
		self.x = x
		self.y = y


	def add_other(self, B):
		# adds a different position to the current position and stores the 
		# result in self. So, if A and B are positions, A.add_other(B) will 
		# change A by adding on position B. To add positions, add up the 
		# x coordinates and the y coordinates.
		self.x += B.x
		self.y += B.y

	
	def up(self):
		# moves the position up by adding 1 to self.x. 
		self.x +=1
#		# For this lab, you don’t need matching down, left and right methods, but it would be a nice touch.


	def print(self):
		print("(", self.x, "," , self.y , ")")
		# which prints out the position in this format: (5,2)

A = Position(1, 1)
B = Position(2, 3)
A.print()
B.print()
A.add_other(B)
A.print()
A.up()	
A.print()
C = Position(-3, -8)
A.add_other(C)
A.print()