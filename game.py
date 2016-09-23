import pygame #DUH
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from bad_guy import Bad_guy #bring in the bad_guy class
from start_button import Play_button


# Set up the main core function
def run_game():
	pygame.init() #initialize all the pygame modules
	game_settings = Settings() #create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) #Set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	
	#music 
	pygame.mixer.music.load('.wav')
	pygame.mixer.music.play(-1)
	
	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	bad_guy = Bad_guy(screen)
	bullets = Group() #set the bullets to group
	#create a play button object and assign to a var
	play_button = Play_button(screen, 'Play Game')

	

	while 1: #run this loop forever...
		gf.check_events(hero, bullets, game_settings, screen, bad_guy, play_button) #call gf (aliased from game_functions module) and get the check_events method
		gf.update_screen(game_settings, screen, hero, bullets, bad_guy, play_button) #call the update_screen method which handles updating the screen
		print bool(theDict)
		if (theDict):
			print "Some music for a different hit"
		if(game_settings.game_active):
			hero.update() #update the hero flags
			bad_guy.update()		
			bullets.update() #call the update method in the while loop
			


run_game() #Start the game!