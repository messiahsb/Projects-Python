#imports
import pygame
import random

#display dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#game dimensions
BLOCK_SIZE = 30 
GRID_WIDTH = 10 
GRID_HEIGHT = 20 
BORDER_WIDTH = 4

#colors
BLACK  = (0,0,0)
WHITE = (255, 255, 255) 
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128) 

SHAPES = [
    [1, 1, 1, 1],  #I Shape

    [[1, 1], #O shape
     [1, 1]],

    [[0,1,0] #T shape
     [1,1,1]],

    [[1,1,0] #Z shape
     [0,1,1]],

    [[0,1,1] #S shape
     [1,1,0]],

    [[1,0,0] #J shape
     [1,1,1]],

    [[0,0,1] #L shape
     [1,1,1]],
]
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

class Tetris():
    pass