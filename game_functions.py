#we will put all main game function here
import sys # we will need the  sys so users to be able to quit
import pygame
from bullets import Bullet #we dont care about the update or draw functions. Just the bullets

def check_events(hero,bullets, screen, game_settings):
	for event in pygame.event.get(): #runn through all pygame events
		if event.type == pygame.QUIT: #if evetn is quit event, 
			sys.exit() #QUIT
		elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
			#print event.key
			if event.key == pygame.K_RIGHT: #the user pressed right
				hero.moving_right = True #set the flag
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True #set the flag
			elif event.key == pygame.K_SPACE: #user pushed the spacebar
				new_bullet =  Bullet(screen, hero, game_settings)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP: #uder let go of the key
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False





#handle all screen updates
def update_screen(settings, screen,hero,bullets):
	screen.fill(settings.bg_color) # fill the background with the green
	hero.draw_me() #call the draw method and put the hero on the screen
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()
