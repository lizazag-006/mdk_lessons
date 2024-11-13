
import pygame
from pygame.locals import *
class Square(pygame.sprite.Sprite):
	def __init__(self):
		super(Square, self).__init__()
		self.surf = pygame.Surface((25, 25))
		self.surf.fill((0, 200, 255))
		self.rect = self.surf.get_rect()

pygame.init()

screen = pygame.display.set_mode((800, 600))


square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()


gameOn = True


while gameOn:
	
	for event in pygame.event.get():
		
		if event.type == KEYDOWN:
			

			if event.key == K_BACKSPACE:
				gameOn = False
				

		elif event.type == QUIT:
			gameOn = False

	screen.blit(square1.surf, (40, 40))
	screen.blit(square2.surf, (40, 530))
	screen.blit(square3.surf, (730, 40))
	screen.blit(square4.surf, (730, 530))

	pygame.display.flip()
import pygame 

pygame.init() 

canvas = pygame.display.set_mode((500, 500)) 

pygame.display.set_caption("My Board") 
exit = False

while not exit: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = True
	pygame.display.update() 

import pygame 

pygame.init() 

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0) 
red = (255, 0, 0) 

X = 400
Y = 400
 
display_surface = pygame.display.set_mode((X, Y )) 

pygame.display.set_caption('Drawing') 

display_surface.fill(white) 

pygame.draw.polygon(display_surface, blue, 
					[(146, 0), (291, 106), 
					(236, 277), (56, 277), (0, 106)]) 
					

pygame.draw.line(display_surface, green, 
				(60, 300), (120, 300), 4) 


pygame.draw.circle(display_surface, 
		green, (300, 50), 20, 0) 


pygame.draw.ellipse(display_surface, black, 
					(300, 250, 40, 80), 1) 

 
pygame.draw.rect(display_surface, black, 
					(150, 300, 100, 50)) 

while True : 
	
	for event in pygame.event.get() : 

		if event.type == pygame.QUIT : 

			pygame.quit() 

			quit() 
		pygame.display.update() 


pygame.init()
surface = pygame.display.set_mode((400,300))
color = (255,0,0)
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()



pygame.init()
surface = pygame.display.set_mode((400, 300))
color = (48, 141, 70)
pygame.draw.rect(surface, color, pygame.Rect(
    30, 30, 60, 60),  2,  border_bottom_right_radius=5) 
pygame.display.flip()
