from pygame import *
from sys import exit
from random import *

class Object:
	def disp(self, screen):
		screen.blit(self.sprite, self.rect)


class Hero(Object):
	def __init__(self):
		self.sprite = image.load('data/hero.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 250
		self.rect.centery = 350
		self.move_x = 0
		self.move_y = 0

	def up(self):
		self.move_y = -5
	def down(self):
		self.move_y = 5
	def stop_y(self):
		self.move_y = 0
	def cycle(self):
		self.rect.centerx += self.move_x
		self.rect.centery += self.move_y

###################################################################################

###################################################################################

class Shield_1(Object):
	def __init__(self):
		self.sprite = image.load('data/shields_3.png')
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 250
		self.rect.centery = 250
	def collision(self, hero):
		if self.rect.colliderect(hero.rect):
			self.sprite = image.load("data/explode.bmp")
		

init()
screen = display.set_mode((500, 500))
hero = Hero()
shield_1 = Shield_1()


while True:

	for e in event.get():
		if e.type == KEYDOWN:
			if e.key == K_UP:
				hero.up()
			if e.key == K_DOWN:
				hero.down()
		if e.type == KEYUP:
			if e.key == K_UP or e.key == K_DOWN:
				hero.stop_y()
		if e.type == QUIT:
			quit()

	shield_1.collision(hero)
	hero.cycle()
	screen.fill((255,255,255))
	hero.disp(screen)
	shield_1.disp(screen)
	display.flip()
	display.update()


	
