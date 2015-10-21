# Project 1 v1.3
# Created by Eric Chen
# Python 2.7.2 / Pygame

import pygame
from pygame import *
from pygame.locals import *
import random


class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = image.load(filename)
		self.bitmap.set_colorkey((0,0,0))
	def set_position(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))


def Intersect(s1_x, s1_y, s2_x, s2_y):
	if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
		return 3
	else:
		return 0
	############################################################################################################################
	#TESTING
#class Bullet(pygame.sprite.Sprite):
#	def __init__(self):
#		pygame.sprite.Sprite.__init__(self)
#		self.image = pygame.Surface([4, 10])
#		self.image.fill(black)

#		self.rect = self.image.get_rect()
	############################################################################################################################

init() # INITIALIZE
screen = display.set_mode((640,480))
key.set_repeat(1, 1)
display.set_caption('Project 1: Pygame')
backdrop = image.load('data/backdrop.png')

enemies = []
enemies_2 = []
#bullet_list = []

shield_1_life = 2
shield_2_life = 2
shield_3_life = 2

x = 0
for count in range(5):
	enemies.append(Sprite(100 * x + 50, 50, 'data/baddie.png'))
	x += 1

y = 0
for count in range(5):
	enemies_2.append(Sprite(100 * y + 50, 150, 'data/baddie_2.png'))
	y += 1

shield = (Sprite(100, 300, 'data/shields_3.png'))
shield_2 = (Sprite(300, 300, 'data/shields_3.png'))
shield_3 = (Sprite(500, 300, 'data/shields_3.png'))
hero = Sprite(20, 400, 'data/hero.png')
bullet = Sprite(0, 480, 'data/heromissile.png')
enemymissile = Sprite(0, 480, 'data/baddiemissile.png')
enemymissile_2 = Sprite(0, 480, 'data/baddiemissile_2.png')

score = 0

quit = 0
enemyspeed = 3
font = pygame.font.SysFont(None, 36)


while quit == 0:
	screen.blit(backdrop, (0, 0))
	score_text = font.render("Your Score: " + str(score), 1, (255, 255, 255))
	screen.blit(score_text, (450, 10))

	############################################################################################################################
	# Enemy Movement

	for count in range(len(enemies)): 
		enemies[count].x += + enemyspeed
		enemies[count].render() # renders enemies/shield   # renders enemies

	if len(enemies) > 0:
		if enemies[len(enemies)-1].x > 590:     
			enemyspeed = -3 					# reached the edge of the screen (590)
			for count in range(len(enemies)):  	# invert the speed and head the other way
				enemies[count].y += 5           # move down 5 pixels vertically # enemy movement
		if enemies[0].x < 10:                   
			enemyspeed = 3
			for count in range(len(enemies)):
				enemies[count].y += 5 # enemy movement 2

	for count in range(len(enemies_2)): 
		enemies_2[count].x += + enemyspeed
		enemies_2[count].render() # renders enemies/shield   # renders enemies

	if len(enemies_2) > 0:
		if enemies_2[len(enemies_2)-1].x > 590:     
			enemyspeed = -3 					# reached the edge of the screen (590)
			for count in range(len(enemies_2)):  	# invert the speed and head the other way
				enemies_2[count].y += 5           # move down 5 pixels vertically # enemy movement
		if enemies_2[0].x < 10:                   
			enemyspeed = 3
			for count in range(len(enemies_2)):
				enemies_2[count].y += 5 # enemy movement 2

	############################################################################################################################

#	for bullet in bullet_list:
#		if bullet.rect.y < -10:
#			bullet_list.remove(bullet)
#			all_sprites_list.remove(bullet)
			
	if bullet.rect.y < 479 and bullet.rect.y > 0: 
		bullet.rect.render()
		bullet.rect.y -= 10     				# subtract 5 from vertical as missile moves up screeen # renders bullet.rect # our missile
		
	if enemymissile.y >= 480 and len(enemies) > 0:   # if missile in play
		enemymissile.x = enemies[random.randint(0, len(enemies) - 1)].x # random enemy from
		enemymissile.y = enemies[0].y           # enemy 0 to last enemy

	if enemymissile_2.y >= 480 and len(enemies_2) > 0:   # if missile in play
		enemymissile_2.x = enemies_2[random.randint(0, len(enemies_2) - 1)].x # random enemy from
		enemymissile_2.y = enemies_2[0].y	

	if Intersect(hero.x, hero.y, enemymissile.x, enemymissile.y): # if collision is detected, quit
		quit = 1

	if Intersect(hero.x, hero.y, enemymissile_2.x, enemymissile_2.y): # if collision is detected, quit
		quit = 1

	if quit == 1:
		you_lose_text = font.render("You Lose", 1, (255, 255, 255))
		screen.blit(you_lose_text, (260, 300))

	for count in range(0, len(enemies)):
		if Intersect(bullet.rect.x, bullet.rect.y, enemies[count].x, enemies[count].y):
			del enemies[count]					# if enemies intersect with missile, delete them
			bullet.rect.x = 0
			bullet.rect.y = 720
			score += 1
			break

	for count in range(0, len(enemies_2)):
		if Intersect(bullet.rect.x, bullet.rect.y, enemies_2[count].x, enemies_2[count].y):
			del enemies_2[count]
			bullet.rect.x = 0
			bullet.rect.y = 720
			score += 1
			break

	############################################################################################################################
	# Shield Interactions

	if Intersect(enemymissile.x, enemymissile.y, shield.x, shield.y):
		if shield_1_life > 0:
			shield_1_life -= 1
			enemymissile.x = 0
			enemymissile.y = 480
		if shield_1_life == 0:
			shield.x = 0
			shield.y = 480
			enemymissile.x = 0
			enemymissile.y = 480 # IF THEY HIT SHIELD # if enemy hits shield

	if Intersect(enemymissile_2.x, enemymissile_2.y, shield.x, shield.y):
		if shield_1_life > 0:
			shield_1_life -= 1
			enemymissile_2.x = 0
			enemymissile_2.y = 480
		if shield_1_life == 0:
			shield.x = 0
			shield.y = 480
			enemymissile_2.x = 0
			enemymissile_2.y = 480 # IF THEY HIT SHIELD # if enemy_2 hits shield

	if Intersect(bullet.rect.x, bullet.rect.y, shield.x, shield.y):
		if shield_1_life > 0:
			shield_1_life -= 1
			bullet.rect.x = 0
			bullet.rect.y = 480
		if shield_1_life == 0:	
			shield.x = 0
			shield.y = 480
			bullet.rect.x = 0
			bullet.rect.y = 480 # if we hit shield


	if Intersect(enemymissile.x, enemymissile.y, shield_2.x, shield_2.y):
		if shield_2_life > 0:
			shield_2_life -= 1
			enemymissile.x = 0
			enemymissile.y = 480
		if shield_2_life == 0:
			shield_2.x = 0
			shield_2.y = 480
			enemymissile.x = 0
			enemymissile.y = 480 # IF THEY HIT SHIELD 2 # if enemy hits shield 2

	if Intersect(enemymissile_2.x, enemymissile_2.y, shield_2.x, shield_2.y):
		if shield_2_life > 0:
			shield_2_life -= 1
			enemymissile_2.x = 0
			enemymissile_2.y = 480
		if shield_2_life == 0:
			shield_2.x = 0
			shield_2.y = 480
			enemymissile_2.x = 0
			enemymissile_2.y = 480 # IF THEY HIT SHIELD 2 # if enemy 2 hits shield 2

	if Intersect(bullet.rect.x, bullet.rect.y, shield_2.x, shield_2.y):
		if shield_2_life > 0:
			shield_2_life -= 1
			bullet.rect.x = 0
			bullet.rect.y = 480
		if shield_2_life == 0:
			shield_2.x = 0
			shield_2.y = 480
			bullet.rect.x = 0
			bullet.rect.y = 480 # if we hit shield 2


	if Intersect(enemymissile.x, enemymissile.y, shield_3.x, shield_3.y):
		if shield_3_life > 0:
			shield_3_life -= 1
			enemymissile.x = 0
			enemymissile.y = 480
		if shield_3_life == 0:
			shield_3.x = 0
			shield_3.y = 480			
			enemymissile.x = 0
			enemymissile.y = 480 # IF THEY HIT SHIELD 3 # if enemy hits shield 3

	if Intersect(enemymissile_2.x, enemymissile_2.y, shield_3.x, shield_3.y):
		if shield_3_life > 0:
			shield_3_life -= 1
			enemymissile_2.x = 0
			enemymissile_2.y = 480
		if shield_3_life == 0:
			shield_3.x = 0
			shield_3.y = 480			
			enemymissile_2.x = 0
			enemymissile_2.y = 480 # IF THEY HIT SHIELD 3 # if enemy 2 hits shield 3

	if Intersect(bullet.rect.x, bullet.rect.y, shield_3.x, shield_3.y):
		if shield_3_life > 0:
			shield_3_life -= 1
			bullet.rect.x = 0
			bullet.rect.y = 480
		if shield_3_life == 0:
			shield_3.x = 0
			shield_3.y = 480			
			bullet.rect.x = 0
			bullet.rect.y = 480# if we hit shield 3
	
	############################################################################################################################	


	if len(enemies) + len(enemies_2) == 0: 					
		you_win_text = font.render("You Win", 1, (255, 255, 255))
		screen.blit(you_win_text, (260, 300))

	for ourevent in event.get():
		if ourevent.type == QUIT: 				
			quit = 1
		if ourevent.type == KEYDOWN:
			if ourevent.key == K_RIGHT and hero.x < 590: 
				hero.x += 5
			if ourevent.key == K_LEFT and hero.x > 10: 
				hero.x -= 5
			if ourevent.key == K_SPACE:
				bullet.rect.x = hero.x 			
				bullet.rect.y = hero.y 


	enemymissile.render() 						
	enemymissile_2.render()
	enemymissile.y += 5
	enemymissile_2.y += 5

	hero.render()
	shield.render()
	shield_2.render()
	shield_3.render()


	display.update() 							
	time.delay(5) 								
	clock.tick(20)
