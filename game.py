import pygame #DUH
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from bad_guy import Bad_guy #bring in the bad_guy class

# Set up the main core function
def run_game():
	pygame.init() #initialize all the pygame modules
	game_settings = Settings() #create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) #Set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	bad_guy = Bad_guy(screen)
	bullets = Group() #set the bullets to group

	while 1: #run this loop forever...
		gf.check_events(hero, bullets, game_settings, screen, bad_guy) #call gf (aliased from game_functions module) and get the check_events method
		hero.update() #update the hero flags
		bad_guy.update()		
		bullets.update() #call the update method in the while loop
		gf.update_screen(game_settings, screen, hero, bullets, bad_guy) #call the update_screen method which handles updating the screen


run_game() #Start the game!