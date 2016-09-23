# We will put all main game functions here
import sys #we will need sys so the user can quit
import pygame
from bullets import Bullet #we dont care about the update or draw functions. Just the class

def check_events(hero, bullets, game_settings, screen, bad_guy, play_button):
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT: #if the event is the quit event...
			sys.exit() #quit
		#handle button click
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if play_button.rect.collidepoint(mouse_x,mouse_y):
				# print "User clicked the button"
				game_settings.game_active = True
		elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
			if event.key == pygame.K_RIGHT: #the user pressed right
				hero.moving_right = True #set the flag
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True #set the flag
			elif event.key == pygame.K_SPACE: #user pushed space bar
				new_bullet = Bullet(screen, hero, game_settings)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP: #user let go of a key
			if event.key == pygame.K_RIGHT: #specifically the right arrow
				hero.moving_right = False
			elif event.key == pygame.K_LEFT: #specifically the left arrow
				hero.moving_left = False
			


# Handle all the screen updates and drawing
def update_screen(settings, screen, hero, bullets, bad_guy, play_button):

	screen.fill(settings.bg_color)# Fill the background with our color
	hero.draw_me() #call the draw method and put the hero on the screen
	bad_guy.draw_me()
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	if not settings.game_active:
		play_button.draw_button()

	pygame.display.flip()