from pygame import *

size_x = 1000
size_y = 1000

class Object:
	def disp(self, screen):
		screen.blit(self.sprite, self.rect)

class Cat(Object):
	def __init__(self):
		self.sprite = image.load("cat.bmp")
		self.rect = self.sprite.get_rect()
		self.rect.centerx = size_x / 2
		self.rect.centery = size_y / 2

	def chase(self, mouse):
		if mouse.rect.centerx > self.rect.centerx:
			self.rect.centerx += 5
		if mouse.rect.centerx < self.rect.centerx:
			self.rect.centerx -= 5
		if mouse.rect.centery > self.rect.centery:
			self.rect.centery += 5
		if mouse.rect.centery < self.rect.centery:
			self.rect.centery -= 5
		# TODO:  Fill in chasing code here
		# This code should move the cat toward the mouse
		# If the mouse is above the cat, move the cat up
		# If the mouse is below the cat, move it down
		# Same for right and left
		# This may give the cat a speed increase when moving at a diagonal

class Mouse(Object):
	def __init__(self):
		self.sprite = image.load("mouse.bmp")
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 100
		self.move_x = 0
		self.move_y = 0

		# Use a "move" variable like in pygame_demo on the class website
		# But, you need to handle moving in both directions!
		# So use two variables, one for x movement, and one for y movement

	# TODO:  Write function bodies for these movement-related methods
	# right, left, up, and down just need to change variables created in __init__
	def right(self):
		self.move_x = 15
	def left(self):
		self.move_x = -15
	def up(self):
		self.move_y = -15
	def down(self):
		self.move_y = 15
# stop_x and stop_y cancel x and y movement (set the movement value to 0)
	def stop_x(self):
		self.move_x = 0
	def stop_y(self):
		self.move_y = 0
	def cycle(self):
		self.rect.centerx += self.move_x
		self.rect.centery += self.move_y

# From here down, the program is complete.
# You might need to look at it to fill in the above methods!
# Uncomment the lines below when you have the related methods complete

init()
screen = display.set_mode((size_x, size_y))
c = Cat()
m = Mouse()
clock = time.Clock()

while True:
	for e in event.get():
		if e.type == QUIT:
			quit()
		if e.type == KEYDOWN:
			if e.key == K_RIGHT:
				m.right()
			elif e.key == K_LEFT:
				m.left()
			elif e.key == K_UP:
				m.up()
			elif e.key == K_DOWN:
				m.down()
		if e.type == KEYUP:
			if e.key == K_RIGHT or e.key == K_LEFT:
				m.stop_x()
			if e.key == K_UP or e.key == K_DOWN:
				m.stop_y()
	
	c.chase(m)
	m.cycle()
	screen.fill((255,255,255))
	m.disp(screen)
	c.disp(screen)
	display.flip()
	clock.tick(60)
