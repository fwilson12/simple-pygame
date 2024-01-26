# Import the pygame library
from pygame import mixer
import pygame, random

from sys import exit

# Necessary Step! Initiates all of the parts of the Pygame library.
pygame.init()

# Create Screen - a display surface
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

# Add a label to the pygame window
pygame.display.set_caption("Intro to Pygame: Platform Game")

# Create Clock object - responsible for controlling the games frame rate
clock = pygame.time.Clock() # create a clock object


class Background(pygame.sprite.Sprite):
	def __init__(self, image_path, x, y, speed):
		super().__init__()
		self.x = x
		self.y = y
		self.speed = speed
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect(center = (self.x, self.y))

	def move_right(self):
		if self.rect.centerx > 1200:
			self.x = -400
			self.rect.centerx = self.x
		self.x += self.speed
		self.rect.centerx = self.x

	def move_left(self):
		if self.rect.centerx < -400:
			self.x = 1200
			self.rect.center = (self.x,self.y)
		self.x -= self.speed
		self.rect.center = (self.x,self.y)

class Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Player,self).__init__()
		self.moveY = 0
		self.x = x
		self.y = y
		self.index = 0
		self.direction = "right"
		self.right_files = ["ye right.png"]
		self.right_images = [pygame.image.load(filename).convert_alpha() for filename in self.right_files]
		self.pics = [[pygame.image.load("ye straight 2.png")],[pygame.transform.flip(img, True, False) for img in self.right_images], [pygame.image.load(filename).convert_alpha() for filename in self.right_files]]
		self.image = self.pics[2][0]
		self.rect = self.image.get_rect(center = (self.x, self.y))


	def move_right(self):
		self.direction = "right"
		self.image = self.pics[2][0]
		self.rect.center = (self.x,self.y)
	def move_left(self):
		self.direction = "left"
		self.image = self.pics[1][0]
		self.rect.center = (self.x,self.y)
	def stand(self):
		self.image = self.pics[0][0]
	



'''
Groups
'''
background = pygame.sprite.Group() # Contains images of the blue sky and mountains
background.add(Background("backgroud.jpg",-400,150, 4))
background.add(Background("backgroud.jpg",400,150, 4))
background.add(Background("backgroud.jpg",1200,150, 4))


land = pygame.sprite.Group() # Contains the platform images that the player run/walks on
land.add(Background("ground - Copy.png",325,425,8))
land.add(Background("short_ground - Copy.png",1100,425,8))

scenery = pygame.sprite.Group() # Contains both the background and platform images
scenery.add(background)
scenery.add(land)

player = Player(200,100)

all_sprites = pygame.sprite.Group() #contains all surfaces
all_sprites.add(scenery)
all_sprites.add(player)

while True:
	#Event loop - Looks for for user input which could include: key presses, mouse movement, mouse clicks, etc.
	for event in pygame.event.get():
		# Close game if the red square in the top left of the window is clicked
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		# Actions that the player takes when the user lifts finger from keys
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				player.stand()
			if event.key == pygame.K_LEFT:
				player.stand()
			if event.key == pygame.K_UP:
				player.stand()
	# Actions that the player and scenery take when the user presses particular keys	
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
