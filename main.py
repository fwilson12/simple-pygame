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

pygame.display.set_caption("Kanye West tries his Kanye Best to secure flying coins by making a Kanye Catch")

clock = pygame.time.Clock() 



class Player(pygame.sprite.Sprite):
	def __init__(self,x,y, score):
		super(Player,self).__init__()

		self.x = x
		self.y = y
		self.score = score
		self.index = 0
		self.direction = "right"
		self.pics = [pygame.image.load("kanye still.png"), pygame.image.load("kanye right.png"), pygame.image.load("kanye left.png"), pygame.image.load("kanye up.png"), pygame.image.load("kanye down.png")]
		self.image = self.pics[0]
		self.rect = self.image.get_rect(center = (self.x, self.y))


	def move_right(self, deltax):
		
		if self.rect.right>1396:
			deltax = -4
		self.rect.x += deltax
		self.image = self.pics[1]
	
	def move_left(self, deltax):
		if self.rect.left < 4:
			deltax = 4
		self.rect.x += deltax
		self.image = self.pics[2]
	
	def move_up(self, deltay):
		if self.rect.top < 4:
			deltay = 4
		self.rect.y += deltay
		self.image = self.pics[3]
	
	def move_down(self, deltay):
		if self.rect.bottom>796:
			deltay = -4
		self.rect.y += deltay
		self.image = self.pics[4]
	
	def still(self):
		self.image = self.pics[0]
	
	def collision_multi(self, others):
		if pygame.sprite.spritecollide(self, others, False):
			return True
	
	def collision_singular(self, coin):
		if self.rect.colliderect(coin.rect):
			return True
	def display_score(self):
		font = pygame.font.SysFont(None, 55)
		text = font.render("Coins: "+str(self.score), True, 'blue', 'white')
		screen.blit(text, (1200, 750))
		pygame.display.flip()
	def yay_you_win(self):
		font = pygame.font.SysFont(None, 55)
		text = font.render("congrats dude you got a lot of coins and won this little game.", True, 'white', 'blue')
		screen.blit(text, (150, screen_height // 2 - text.get_height()))
		pygame.display.flip()
		pygame.time.delay(2000)
	def boo_you_lose(self):
		font = pygame.font.SysFont(None, 55)
		text = font.render(" you died man you hit the block when you probably should not have.", True, 'white', 'red')
		screen.blit(text, (50, screen_height // 2 - text.get_height()))
		pygame.display.flip()
		pygame.time.delay(2000)
		
		
	



class Block(pygame.sprite.Sprite):
	def __init__(self, x, y, orientation):
		super(Block, self).__init__()
		
		self.orientation = orientation
		self.x = x
		self.y = y
		self.index = 0
		self.pics = [pygame.image.load("red one.png"), pygame.image.load("red two.png"), pygame.image.load("yellow one.png"), pygame.image.load("yellow two.png")]
		if self.orientation == 'vertical':
			self.image = self.pics[0]
		elif self.orientation == 'horizontal':
			self.image = self.pics[1]
		self.rect = self.image.get_rect(topleft = (self.x, self.y))

	def flicker(self):
		num = random.randint(0,100)
		if self.orientation == 'vertical':
			if num <= 5:
				self.index = random.choice([0,2])
				self.image = self.pics[self.index]
				self.rect.topleft = (self.x,self.y)
		elif self.orientation == 'horizontal':
			if num <= 5:
				self.index = random.choice([1,3])
				self.image = self.pics[self.index]
				self.rect.topleft = (self.x,self.y)


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(Coin, self).__init__()

		self.x = x
		self.y = y
		self.index = 0
		self.pics = [pygame.image.load('golden 1.png'), pygame.image.load('golden 2.png')]
		self.image = self.pics[0]
		self.deltax = random.choice([-2,2])
		self.deltay = random.choice([-2,2])
		self.rect = self.image.get_rect(center = (self.x, self.y))
	
	def move(self):
		# print(self.deltax, self.deltay)
		if self.rect.left <= 2 or self.rect.right >= 1398:
			self.deltax *= -1
		if self.rect.top <= 2 or self.rect.bottom >= 798:
			self.deltay *= -1
		
		self.rect.centerx += self.deltax
		self.rect.centery += self.deltay
		
		if random.randint(0,100) <= 4:
			self.index = (self.index +1)%2
		self.image = self.pics[self.index]
		# self.rect.center = (self.x,self.y)


	def relocate(self):
		self.rect.x, self.rect.y = random.randint(600,1300),random.randint(30, 700)


yeezy = Player(80, 150, 0)

players = pygame.sprite.Group()
players.add(yeezy)



coins = pygame.sprite.Group()
for i in range(3):
	coins.add(Coin(random.randint(600,1300),random.randint(100,700)))

blocks = pygame.sprite.Group()
blocks.add(Block(600,0, 'vertical'))
blocks.add(Block(600,150, 'vertical'))
blocks.add(Block(650,300, 'horizontal'))
blocks.add(Block(0,700, 'horizontal'))
blocks.add(Block(500,300, 'horizontal'))
blocks.add(Block(1200,0, 'vertical'))
blocks.add(Block(-80,340, 'horizontal'))
blocks.add(Block(1170,600, 'horizontal'))

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
		yeezy.move_left(-4)
	if keys[pygame.K_RIGHT]:
		yeezy.move_right(4)
	if keys[pygame.K_UP]:
		yeezy.move_up(-4)
	if keys[pygame.K_DOWN]:
		yeezy.move_down(4)

	
	screen.blit(bg, (0,0))
	
	
	for block in blocks:
		block.flicker()
	blocks.draw(screen)

	for coin in coins:
		coin.move()
	coins.draw(screen)
	
	
	if yeezy in players:
		players.draw(screen)
		yeezy.display_score()
		
	if yeezy.collision_multi(blocks) == True:
		yeezy.kill()
		yeezy.boo_you_lose()
	
	for coin in coins:
		if yeezy.collision_singular(coin) == True:
			coin.relocate()
			yeezy.score +=1
	if yeezy.score == 25:
		yeezy.yay_you_win()

	
	pygame.display.update()

	clock.tick(60)
