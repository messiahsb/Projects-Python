#imports
import pygame
import random
import sys

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

    [[0,1,0], #T shape
     [1,1,1]],

    [[1,1,0], #Z shape
     [0,1,1]],

    [[0,1,1], #S shape
     [1,1,0]],

    [[1,0,0],  #J shape
     [1,1,1]],

    [[0,0,1],   #L shape
     [1,1,1]]
]

FPS = 60
#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pytris")
clock = pygame.time.Clock()

game_grid = [[0 for i in range(GRID_WIDTH)] for j in range(GRID_HEIGHT)]
for row in game_grid:
    for col in row:
        print(col, end=" ") # print each element separated by space
    print() # Add newline

# draw the grid of the game on the screen
def drawGrid():
    for x in range(GRID_WIDTH): 
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
 
# game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         game.move_left()

    #fill screen with black
    screen.fill(BLACK)
    drawGrid()
    #update display
    pygame.display.flip()

    
pygame.quit()
sys.exit()


def move_left():
    pass
def move_right():
    pass
def soft_drop(): 
    pass
def hard_drop(): 
    pass


class Piece(object):
    pass

class Tetris():
    pass

