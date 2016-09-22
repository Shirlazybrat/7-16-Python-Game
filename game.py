import sys # we will need the usere to be able to quit
import pygame #duh! The name of the game
from hero import Hero #bring in the hero class wi th all it's methods


# Set up the main core function
def run_game():
	pygame.init() #initialixe  all the pygame modules
	screen = pygame.display.set_mode((1000, 800)) #set the screen size withscreen mode
	pygame.display.set_caption("Monster Attack") #set the message on the ststus bar

	bg_color = (82,111,53) #green grass color

	hero = Hero(screen) #set a variable = to the class and pass it the screen

	while 1: #run thin loop forever
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.ext()

		# fill the background with the green
		screen.fill(bg_color)
		hero.draw_me() #call the draw method and put the hero on the screen
		pygame.display.flip()
	


run_game() #start the game