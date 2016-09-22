
import pygame #duh! The name of the game
from hero import Hero #bring in the hero class wi th all it's methods
from settings import Settings
import game_functions as gf


# Set up the main core function
def run_game():
	pygame.init() #initialixe  all the pygame modules
	game_settings = Settings() #creat
	screen = pygame.display.set_mode(game_settings.screen_size) #set the screen size withscreen mode
	pygame.display.set_caption("Monster Attack") #set the message on the ststus bar

	bg_color = (82,111,53) #green grass color

	hero = Hero(screen) #set a variable = to the class and pass it the screen

	while 1: #run thin loop forever
		gf.check_events(hero) #call gf (aliased from game_function module) and get the check evente method
		gf.update_screen(game_settings, screen, hero) #call this method that updates the screen
	


run_game() #start the game