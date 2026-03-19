#imports
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK  = (0,0,0)
#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pytris")

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with black
    screen.fill(BLACK)

    #update display
    pygame.display.flip()

    
pygame.quit()



class Piece(object):
    pass    