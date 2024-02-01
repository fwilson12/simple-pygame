# Import the pygame library
from pygame import mixer
import pygame, random

from sys import exit

pygame.init()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Coin Hunter")

clock = pygame.time.Clock() 


class Background(pygame.sprite.Sprite):
	def __init__(self, image_path, x, y, speed):
		super().__init__()
		self.x = x
		self.y = y
		self.speed = speed
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect(center = (self.x, self.y))


class Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Player,self).__init__()

		self.x = x
		self.y = y
		self.index = 0
		self.direction = "right"
		self.pics = [[pygame.image.load("ye straight 2.png")],[pygame.transform.flip(img, True, False) for img in self.right_images], [pygame.image.load(filename).convert_alpha() for filename in self.right_files]]
		self.image = self.pics[0][0]
		self.rect = self.image.get_rect(center = (self.x, self.y))


	def move_right(self):
		self.direction = "right"
		self.image = self.pics[1][0]
	def move_left(self):
		self.direction = "left"
		self.image = self.pics[3][0]
	def move_up(self):
		self.direction = "up"
		self.image = self.pics[2][0]
	def move_down(self):
		self.direction = "down"
		self.image = self.pics[4][0]
	def still(self):
		self.image = self.pics[0][0]
	def collision_multi(self, others):
		if pygame.sprite.spritecollide(self, others, False):
			return True
	def collision_singular(self, coin):
		if self.rect.colliderect(coin.rect):
			return True
		
	



class Blocks(pygame.sprite.Sprite):
	def init(self, x,y):
		super(Blocks, self).__init__()

		self.x = x
		self.y = y
		self.index = 0
		self.pics = [pygame.image.load(), pygame.image.load()]
		self.image = self.pics[0]
		self.rect = self.image.get_rect(center = (self.x, self.y))

	def flicker(self):
		num = random.rantint(0,100)
		if num <= 10:
			self.index = (self.index +1)%2
			self.image = self.pics[self.index]
			self.rect.center = (self.x,self.y)

class Coin(pygame.sprite.Sprite):
	def init(self, x, y):
		super(Coin, self).__init__()

		self.x = x
		self.y = y
		self.index = 0
		self.pics = [pygame.image.load(), pygame.image.load(), pygame.image.load()]
		self.image = self.pics[0]
		self.rect = self.image.get_rect(center = (self.x, self.y))
	
	def move(self):
		deltax = random.choice[-2,-1,0,1,2]
		deltay = random.choice[-2,-1,0,1,2,3]
		
		self.rect.centerx += deltax
		self.rect.centery += deltay


'''
Groups
'''
background = pygame.sprite.Group() 
background.add(Background("backgroud.jpg",1200,150, 4))


land = pygame.sprite.Group() 
land.add(Background("ground - Copy.png",325,425,8))
land.add(Background("short_ground - Copy.png",1100,425,8))

scenery = pygame.sprite.Group() 
scenery.add(background)
scenery.add(land)

player = Player(200,100)

all_sprites = pygame.sprite.Group() 
all_sprites.add(scenery)
all_sprites.add(player)

while True:
	
	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				player.stand()
			if event.key == pygame.K_LEFT:
				player.stand()
			if event.key == pygame.K_UP:
				player.stand()
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		for s in scenery:
			s.move_left()
		player.move_right()	
	if keys[pygame.K_LEFT]:
		for s in scenery:
			s.move_right()
		player.move_left()
	


	# The player falls if it is not touch a platform
	

    # Blits all surfaces to screen
	all_sprites.draw(screen)

	# Updates all of the images and objects on the screen (display surface)
	pygame.display.update()

	clock.tick(60)
