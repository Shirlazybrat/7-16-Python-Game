import pygame

class Hero(object):
	def __init__(self, screen):
		self.screen = screen # gice the hero the ability to control the screen

		#load teh hero image, get it's rect
		self.image = pygame.image.load('images/ball.gif')
		self.rect = self.image.get_rect() #pygame gives us get_rect on an y object se we
		self.screen_rect = screen.get_rect() #assign a var so the hero class know how big

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
		self.rect.bottom = self.screen_rect.bottom #this will put our hero bottom at the bottom of the screen
		# not self.rect.sentery because we want the bottom on the bottom

def draw_me(self):
	self.screen.blit(source = self.image, dest = self.rect) #draw the surface...(the image, the where)
