import pygame

class Bad_guy(object):
	def __init__(self, screen):
		self.screen = screen # give the bad_guy the ability to control the screen

		#load teh bad_guy image, get it's rect
		self.image = pygame.image.load('images/witch.gif')
		self.rect = self.image.get_rect() #pygame gives us get_rect on an y object se we
		self.screen_rect = screen.get_rect() #assign a var so the bad_guy class know how big

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the bad_guy at the middle of the screen
		self.rect.top = self.screen_rect.top #this will put our bad_guy top at the top of the screen
		# not self.rect.sentery because we want the top on the top

		#setup movement booleans
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = True

	#add update to the bad_guy class to keep all the updates in the bad_guy class
	def update(self):
		if self.moving_up and self.rect.up < self.screen_rect.up:
			self.rect.centerx += 10 #move the ebad_guy up
		elif self.moving_down and self.rect.down < self.screen_rect.down:
			self.rect.centerx -= 10 #move the bad_guy down
		


	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect) #draw the surface...(the image, the where)
