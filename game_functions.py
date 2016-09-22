#we will put all main game function here
import sys # we will need the  sys so users to be able to quit
import pygame

def check_events(hero):
	for event in pygame.event.get(): #runn through all pygame events
		if event.type == pygame.QUIT: #if evetn is quit event, 
			sys.ext() #QUIT
		elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
			#print event.key
			if event.key == pygame.K_RIGHT: #the user pressed right
				#move the hero to the right
				hero.rect.centerx += 1
			elif event.key == pygame.K_LEFT:
				hero.rect.centerx -= 1




#handle all screen updates
def update_screen(settings, screen,hero):
	screen.fill(settings.bg_color) # fill the background with the green
	hero.draw_me() #call the draw method and put the hero on the screen
	pygame.display.flip()