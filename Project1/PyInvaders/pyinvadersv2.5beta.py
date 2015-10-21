#################### Project 1 v1.0 #######################
################# Created by Eric Chen ####################
############# Python 2.7.2 / Pygame 1.9.1 #################


from pygame import *
from sys import exit
from pygame.locals import *
import random

size_x = 420
size_y = 720

enemies = []
num_list = [1,2,3,4,5,6,7,8,9,10,]
#Bullet = []

class Object:
	def disp(self, screen):
		screen.blit(self.sprite, self.rect)

class Lives(Object):
	def __init__(self):
		self.sprite = image.load('data/lives.png')
	
class Enemy(Object):
	def __init__(self):
		self.sprite = image.load('data/baddie.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 78
		self.rect.centery = 100
		self.speed = 2
		self.life = 1

	def collision(self, b):
		if self.rect.colliderect(b.rect):
			b.rect.centerx = -100
			b.rect.centery = -100
			self.life -= 1
			if self.life == 0:
				self.rect.centery = 10000

	def cycle(self):
		self.rect.centerx += self.speed
		if self.rect.centerx > 400:
			self.speed = -2
			self.rect.centery += 5
		if self.rect.centerx < 20:
			self.speed = 2
			self.rect.centery += 5

	def append():
		for each in range(10):
			enemies.append(Enemy())
			enemies[each].rect.centerx = num_list[each] * 30
			enemies[each].rect.centery = 20


class Enemybullet(Object):
	def __init__(self):
		self.sprite = image.load('data/baddiemissile.png')
		self.rect = self.sprite.get_rect()
		self.alreadyhit = 0
		self.rect.centerx = -200
		self.rect.centery = -200
		self.move_y = 10
		self.move_x = 0

	def cycle(self):
		self.rect.centery += self.move_y

class Hero(Object):
	def __init__(self):
		self.sprite = image.load('data/hero.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = size_x - 400
		self.rect.centery = 670
		self.hp = 3
		self.move_x = 0
		self.move_y = 0
#	def cycle(self, Enemybullet):
#		self.rect.centery += self.move_y
#		self.rect.centerx += self.move_x
#		if self.hp == 0:
#			you_lose_text = font.render("You Lose", 1, (255, 255, 255))
#			screen.blit(you_lose_text, (size_x/2, size_y/2))
	def left(self):
		self.move_x = -6
	def right(self):
		self.move_x = 6
	def stop_x(self):
		self.move_x = 0
	def stop_y(self):
		self.move_y = 0
	def cycle(self):
		self.rect.centerx += self.move_x


class Bullet(Object):
	def __init__(self):
		self.sprite = image.load('data/heromissile.png')
		self.rect = self.sprite.get_rect()
		self.alreadyhit = 0
		self.rect.centerx = -100
		self.rect.centery = -100

class Shield_1(Object):
	def __init__(self):
		self.sprite = image.load('data/shields_3.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 74.5
		self.rect.centery = 600
		self.life = 2
	def collision(self, b):
		if self.rect.colliderect(b.rect):
			b.rect.centerx = -100
			b.rect.centery = -100
			self.life -= 1
			if self.life == 1:
				self.sprite = image.load('data/damagedshield.png')	
			if self.life == 0:
				self.rect.centery = 10000

class Shield_2(Object):
	def __init__(self):
		self.sprite = image.load('data/shields_3.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 210
		self.rect.centery = 600
		self.life = 2
	def collision(self, b):
		if self.rect.colliderect(b.rect):
			b.rect.centerx = -100
			b.rect.centery = -100
			self.life -= 1
			if self.life == 1:
				self.sprite = image.load('data/damagedshield.png')	
			if self.life == 0:
				self.rect.centery = 10000

class Shield_3(Object):
	def __init__(self):
		self.sprite = image.load('data/shields_3.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 334.5
		self.rect.centery = 600
		self.life = 2
	def collision(self, b):
		if self.rect.colliderect(b.rect):
			b.rect.centerx = -100
			b.rect.centery = -100
			self.life -= 1
			if self.life == 1:
				self.sprite = image.load('data/damagedshield.png')	
			if self.life == 0:
				self.rect.centery = 10000

	
	###########################################################################


init()
screen = display.set_mode((size_x,size_y))
h = Hero()
en = Enemy()
b = Bullet()
eb = Enemybullet()
s_1 = Shield_1()
s_2 = Shield_2()
s_3 = Shield_3()
clock = time.Clock()


	###########################################################################
display.set_caption('Project 1 by Eric Chen')
	###########################################################################


while True:
	for e in event.get():
		if e.type == QUIT:
			quit()
		if e.type == KEYDOWN:
			if e.key == K_RIGHT and h.rect.centerx < 401:
				h.right()
			if e.key == K_LEFT and h.rect.centerx > 21:
				h.left()
			if e.key == K_SPACE:
				b.rect.centerx = h.rect.centerx
				b.rect.centery = h.rect.centery
		if e.type == KEYUP:
			if e.key == K_RIGHT or e.key == K_LEFT:
				h.stop_x()

	if b.rect.centery < 725 and b.rect.centery > -20: 
		b.disp(screen)
		b.rect.centery -= 10

	


#	if eb.rect.centery < 725 and eb.rect.centery > -20: 
#		eb.disp(screen)
#		eb.rect.centery += 8

	###########################################################################

	screen.fill((0,0,0))
	h.cycle()			# hero movement
	en.cycle()			# enemy movement

	h.disp(screen)		# display hero
	b.disp(screen)		# display bullet
	s_1.disp(screen)	# display shield 1
	s_2.disp(screen)	# display shield 2
	s_3.disp(screen)	# display shield 3
	en.disp(screen)		# display enemy

	en.collision(b)		# enemy collision w/ bullet
	s_1.collision(b)	# shield 1 collision w/ bullet
	s_2.collision(b)	# shield 2 collision w/ bullet
	s_3.collision(b)	# shield 3 collision w/ bullet

	en.append()

	eb.disp(screen)		# display enemy bullet
	display.flip()		
	clock.tick(60)
