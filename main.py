# Import the pygame library
from pygame import mixer
import pygame, random
from pygame.locals import *
from sys import exit

pygame.init()

screen_width = 1400
screen_height = 800
bg = pygame.image.load("background.png")
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Coin Hunter")

clock = pygame.time.Clock() 



class Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Player,self).__init__()

		self.x = x
		self.y = y
		self.coins = 0 
		self.index = 0
		self.direction = "right"
		self.pics = [pygame.image.load("kanye still.png"), pygame.image.load("kanye right.png"), pygame.image.load("kanye left.png"), pygame.image.load("kanye up.png"), pygame.image.load("kanye down.png")]
		self.image = self.pics[0]
		self.rect = self.image.get_rect(center = (self.x, self.y))


	def move_right(self):
		self.direction = "right"
		self.rect.x += 5
		self.image = self.pics[1]
	def move_left(self):
		self.direction = "left"
		self.rect.x -= 5
		self.image = self.pics[2]
	def move_up(self):
		self.direction = "up"
		self.rect.y -= 5
		self.image = self.pics[3]
	def move_down(self):
		self.direction = "down"
		self.rect.y += 5
		self.image = self.pics[4]
	def still(self):
		self.image = self.pics[0]
	def collision_multi(self, others):
		if pygame.sprite.spritecollide(self, others, False):
			return True
	def collision_singular(self, coin):
		if self.rect.colliderect(coin.rect):
			return True
		
	



class Blocks(pygame.sprite.Sprite):
	def __init__(self, x, y, orientation):
		super(Blocks, self).__init__()
		
		self.orientation = orientation
		self.x = x
		self.y = y
		self.index = 0
		self.pics = [pygame.image.load("red one.png"), pygame.image.load("red two.png"), pygame.image.load("yellow one.png"), pygame.image.load("yellow two.png")]
		if self.orientation == 'vertical':
			self.image = self.pics[0]
		elif self.orientation == 'horizontal':
			self.image = self.pics[1]
		self.rect = self.image.get_rect(center = (self.x, self.y))

	def flicker(self):
		num = random.randint(0,100)
		if self.orientation == 'vertical':
			if num <= 5:
				self.index = random.choice([0,2])
				self.image = self.pics[self.index]
				self.rect.center = (self.x,self.y)
		elif self.orientation == 'horizontal':
			if num <= 5:
				self.index = random.choice([1,3])
				self.image = self.pics[self.index]
				self.rect.center = (self.x,self.y)


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Coin, self).__init__()

		self.x = x
		self.y = y
		self.index = 0
		self.pics = [pygame.image.load('golden 1.png'), pygame.image.load('golden 2.png')]
		self.image = self.pics[0]
		self.rect = self.image.get_rect(center = (self.x, self.y))
	
	def move(self):
		deltax = random.choice([-2,-1,0,1,2])
		deltay = random.choice([-2,-1,0,1,2])
		
		self.rect.centerx += deltax
		self.rect.centery += deltay
	def relocate(self):
		pass


yeezy = Player(screen_width // 2, screen_height // 2)

players = pygame.sprite.Group()
players.add(yeezy)


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				yeezy.still()

	
	
	
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		yeezy.move_left()
	if keys[pygame.K_RIGHT]:
		yeezy.move_right()
	if keys[pygame.K_UP]:
		yeezy.move_up()
	if keys[pygame.K_DOWN]:
		yeezy.move_down()


	
	screen.blit(bg, (0,0))
	if yeezy in players:
		players.draw(screen)
	

	
	pygame.display.update()

	clock.tick(60)
