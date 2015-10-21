# Project 1 v2.0
# Created by Eric Chen
# Custom Version for Mac
# Python 2.7.2 / Pygame

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




#def Intersect(s1_x, s1_y, s2_x, s2_y):
#	if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
#		return 3
#	else:
#		return 0

	############################################################################################################################
	#TESTING. UNSTABLE
#class Bullet(pygame.sprite.Sprite):
#	def __init__(self):
#		pygame.sprite.Sprite.__init__(self)
#		self.image = pygame.Surface([4, 10])
#		self.image.fill(black)

#		self.rect = self.image.get_rect()
	############################################################################################################################

init()
screen = display.set_mode((420,720))
key.set_repeat(1, 1)
display.set_caption('Project 1')
backdrop = image.load('data/backdrop.png')

enemies = []
enemies_2 = []
#bullet_list = []

shield_1_life = 2
shield_2_life = 2
shield_3_life = 2

x = 0
for count in range(5):
	enemies.append(Sprite(58 * x + 20, 100, 'data/baddie.png'))
	x += 1

y = 0
for count in range(5):
	enemies_2.append(Sprite(58 * y + 20, 150, 'data/baddie_2.png'))
	y += 1

shield_1 = (Sprite(43.5, 600, 'data/shields_3.png'))
shield_2 = (Sprite(169, 600, 'data/shields_3.png'))
shield_3 = (Sprite(294.5, 600, 'data/shields_3.png'))
hero = Sprite(20, 670, 'data/hero.png')
hero.rect = hero.sprite.get_rect()
bullet = Sprite(0, 720, 'data/heromissile.png')
enemymissile = Sprite(0, 720, 'data/baddiemissile.png')
enemymissile_2 = Sprite(0, 720, 'data/baddiemissile_2.png')

score = 0
enemyspeed = 2
pause = False

quit = 0
font = font.SysFont(None, 15)


while quit == 0:
	screen.blit(backdrop, (0, 0))
	score_text = font.render("Your Score: " + str(score), 1, (255, 255, 255))
	screen.blit(score_text, (125, 10))

	############################################################################################################################
	# Key Board Controls

	for ourevent in event.get():
		if ourevent.type == QUIT: 				
			quit = 1
		if ourevent.type == KEYDOWN:
			if ourevent.key == K_RIGHT and hero.x < 370: 
				hero.x += 5
			if ourevent.key == K_LEFT and hero.x > 10: 
				hero.x -= 5
			if ourevent.key == K_SPACE:
				bullet.x = hero.x + 23			
				bullet.y = hero.y
			if ourevent.key == K_p:
				pause = False

	while pause == False:
		for ourevent in event.get():
			if ourevent.type == KEYDOWN:
				if ourevent.key == K_p:
					pause = True
	############################################################################################################################
	# Enemy Movement

	for count in range(len(enemies)): 
		enemies[count].x += + enemyspeed
		enemies[count].render() # renders enemies/shield   # renders enemies

	if len(enemies) > 0:
		if enemies[len(enemies)-1].x > 400:     
			enemyspeed = -2					# reached the edge of the screen (590)
			for count in range(len(enemies)):  	# invert the speed and head the other way
				enemies[count].y += 5           # move down 5 pixels vertically # enemy movement
		if enemies[0].x < 20:                   
			enemyspeed = 2
			for count in range(len(enemies)):
				enemies[count].y += 5 # enemy movement 2

	for count in range(len(enemies_2)): 
		enemies_2[count].x += + enemyspeed
		enemies_2[count].render() # renders enemies/shield   # renders enemies

	if len(enemies_2) > 0:
		if enemies_2[len(enemies_2)-1].x > 400:     
			enemyspeed = -2					# reached the edge of the screen (590)
			for count in range(len(enemies_2)):  	# invert the speed and head the other way
				enemies_2[count].y += 5           # move down 5 pixels vertically # enemy movement
		if enemies_2[0].x < 20:                   
			enemyspeed = 2
			for count in range(len(enemies_2)):
				enemies_2[count].y += 5 # enemy movement 2
	############################################################################################################################
	############################################################################################################################

#	for bullet in bullet_list:
#		if bullet.y < -10:
#			bullet_list.remove(bullet)
#			all_sprites_list.remove(bullet)
			
	if bullet.y < 719 and bullet.y > 0: 
		bullet.render()
		bullet.y -= 10
		
	if enemymissile.y >= 720 and len(enemies) > 0: 
		enemymissile.x = enemies[random.randint(0, len(enemies) - 1)].x
		enemymissile.y = enemies[0].y

	if enemymissile_2.y >= 720 and len(enemies_2) > 0:
		enemymissile_2.x = enemies_2[random.randint(0, len(enemies_2) - 1)].x
		enemymissile_2.y = enemies_2[0].y	

	if hero.rect.colliderect(enemymissile.rect):
#		return 3
		quit = 1
#	else:
#		return 0

	if hero.rect.colliderect(enemymissile_2.rect):
#		return 3
		quit = 1
#	else:
#		return 0

	if enemies[count] > 0:
		if enemies[count].y == 700:
			quit = 1
		if enemies_2[count].y == 700:
			quit = 1

	if quit == 1:
		you_lose_text = font.render("You Lose", 1, (255, 255, 255))
		screen.blit(you_lose_text, (150, 350))

	for count in range(0, len(enemies)):
		if bullet.rect.colliderect(enemies.rect):
			del enemies[count]
			bullet.x = 0
			bullet.y = 720
			score += 1
			break

	for count in range(0, len(enemies_2)):
		if bullet.rect.colliderect(enemies_2.rect):
			del enemies_2[count]
			bullet.x = 0
			bullet.y = 720
			score += 1
			break

	############################################################################################################################
	# Shield_1 Interactions

#	if Intersect(enemymissile.x, enemymissile.y, shield_1.x, shield_1.y):
		if shield_1_life > 0:
			shield_1_life -= 1
			enemymissile.x = 0
			enemymissile.y = 720
		else:
			shield_1.x = 0
			shield_1.y = 720
			enemymissile.x = 0
			enemymissile.y = 720

#	if Intersect(enemymissile_2.x, enemymissile_2.y, shield_1.x, shield_1.y):
		if shield_1_life > 0:
			shield_1_life -= 1
			enemymissile_2.x = 0
			enemymissile_2.y = 720
		else:
			shield_1.x = 0
			shield_1.y = 720
			enemymissile_2.x = 0
			enemymissile_2.y = 720

#	if Intersect(bullet.x, bullet.y, shield_1.x, shield_1.y):
		if shield_1_life > 0:
			shield_1_life -= 1
			bullet.x = 0
			bullet.y = 720
		else:
			shield_1.x = 0
			shield_1.y = 720
			bullet.x = 0
			bullet.y = 720
	# Shield_2 Interactions

#	if Intersect(enemymissile.x, enemymissile.y, shield_2.x, shield_2.y):
		if shield_2_life > 0:
			shield_2_life -= 1
			enemymissile.x = 0
			enemymissile.y = 720
		else:
			shield_2.x = 0
			shield_2.y = 720
			enemymissile.x = 0
			enemymissile.y = 720

#	if Intersect(enemymissile_2.x, enemymissile_2.y, shield_2.x, shield_2.y):
		if shield_2_life > 0:
			shield_2_life -= 1
			enemymissile_2.x = 0
			enemymissile_2.y = 720
		else:
			shield_2.x = 0
			shield_2.y = 720
			enemymissile_2.x = 0
			enemymissile_2.y = 720

#	if Intersect(bullet.x, bullet.y, shield_2.x, shield_2.y):
		if shield_2_life > 0:
			shield_2_life -= 1
			bullet.x = 0
			bullet.y = 720
		else:
			shield_2.x = 0
			shield_2.y = 720
			bullet.x = 0
			bullet.y = 720
	# Shield_3 Interactions

#	if Intersect(enemymissile.x, enemymissile.y, shield_3.x, shield_3.y):
		if shield_3_life > 0:
			shield_3_life -= 1
			enemymissile.x = 0
			enemymissile.y = 720
		else:
			shield_3.x = 0
			shield_3.y = 720			
			enemymissile.x = 0
			enemymissile.y = 720

#	if Intersect(enemymissile_2.x, enemymissile_2.y, shield_3.x, shield_3.y):
		if shield_3_life > 0:
			shield_3_life -= 1
			enemymissile_2.x = 0
			enemymissile_2.y = 720
		else:
			shield_3.x = 0
			shield_3.y = 720			
			enemymissile_2.x = 0
			enemymissile_2.y = 720

#	if Intersect(bullet.x, bullet.y, shield_3.x, shield_3.y):
		if shield_3_life > 0:
			shield_3_life -= 1
			bullet.x = 0
			bullet.y = 720
		else:
			shield_3.x = 0
			shield_3.y = 720			
			bullet.x = 0
			bullet.y = 720
	
	############################################################################################################################	


	if len(enemies) + len(enemies_2) == 0: 					
		you_win_text = font.render("You Win", 1, (255, 255, 255))
		screen.blit(you_win_text, (150, 350))

	enemymissile.render() 						
	enemymissile_2.render()
	enemymissile.y += 5
	enemymissile_2.y += 5

	hero.render()
	shield_1.render()
	shield_2.render()
	shield_3.render()

	display.update() 							
	time.delay(10) 								
