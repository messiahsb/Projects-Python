import pygame
import sys
from pygame.math import Vector2
import random

pygame.init()


CELL_SIZE = 30
NUMBER_CELLS = 25
WIN_HEIGHT = WIN_WIDTH = CELL_SIZE*NUMBER_CELLS



screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()


GREEN = (173, 204, 96)
DARK_GREEN = (43, 52, 24)

class Food():
    def __init__(self):
        self.position = Vector2(5,6)
    
    def draw(self):
        food_rect = pygame.Rect(self.position.x*CELL_SIZE, self.position.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, DARK_GREEN, food_rect)

food = Food()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GREEN)
    food.draw()

    pygame.display.update()
    clock.tick(60)