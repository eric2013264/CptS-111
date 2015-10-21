from pygame import *

class Ball:
	def __init__(self):
		self.sprite = image.load("ball.bmp")
		self.rect = self.sprite.get_rect()
		self.rect.centerx = 400
		self.rect.centery = 500
		self.count = 0

	def cycle(self):
		self.rect.centery = 500 - abs(self.count) 
		self.count += 2
		if self.count > 400:
			self.count = -400		

	def disp(self, screen):
		screen.blit(self.sprite, self.rect)

init()
screen = display.set_mode((800,600))
clock = time.Clock()
b = Ball()

while True:
	screen.fill((0,0,0))
	b.cycle()
	b.disp(screen)
	display.flip()
	clock.tick(60)
