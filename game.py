import sys # we will need the usere to be able to quit
import pygame #duh! The name of the game

#setup the main core of the game
def run_game():
	pygame.init()
import sys #we will need sys so the user can quit
import pygame #DUH

# Set up the main core function
def run_game():
	pygame.init()
	size = width, height = 720, 540
	speed = [2, 5]
	black = 0, 0, 0
	screen = pygame.display.set_mode(size)
	ball = pygame.image.load("ball.gif")
	#ballrect = ball.get_rect()
	print ballrect
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]
		screen.fill(black)
		screen.blit(ball, ballrect) #put a surface somewhere
		pygame.display.flip()

run_game() #Start the game!


run_game() #start the game