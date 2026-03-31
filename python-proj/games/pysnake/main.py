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
    def __init__(self, snake):
        self.position = self.gen_new_pos(snake)

    def draw(self):
        food_rect = pygame.Rect(self.position.x*CELL_SIZE, self.position.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.ellipse(screen, 'red', food_rect)

    def gen_new_pos(self, snake):
        pos = Vector2(random.randint(0, NUMBER_CELLS-1), random.randint(0, NUMBER_CELLS-1)) 
        while pos in snake:
            pos = Vector2(random.randint(0, NUMBER_CELLS-1), random.randint(0, NUMBER_CELLS-1)) 
        return pos

class Snake():
    def __init__ (self):
        self.body = [Vector2(8, 5), Vector2(7, 5), Vector2(6, 5)]
        self.direction = Vector2(1,0)
        
    def draw(self):
        for seg in self.body:
            seg_rect = (seg.x * CELL_SIZE, seg.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, DARK_GREEN, seg_rect, 0, 7)
   
    def move_snake(self, dir):
        self.direction = dir
    
    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)


    def grow_body(self):
        self.body.append(self.body[-1] + self.direction)

class Game():
    def __init__(self):
        self.snake = Snake()        
        self.food = Food(self.snake.body)

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        self.snake.update()
        self.check_eat()

    def check_eat(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.gen_new_pos(self.snake.body)
        
    
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

running = True
game = Game()
snake = game.snake
food = game.food

while running:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE: 
                game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction!= Vector2(0,1):
                snake.move_snake(Vector2(0,-1))
            elif event.key == pygame.K_DOWN and snake.direction!= Vector2(0,-1):
                snake.move_snake(Vector2(0,1))
            elif event.key == pygame.K_RIGHT and snake.direction != Vector2(-1,0):
                snake.move_snake(Vector2(1,0))
            elif event.key == pygame.K_LEFT and snake.direction != Vector2(1,0):
                snake.move_snake(Vector2(-1,0))

    
    screen.fill(GREEN)
    game.draw()

    pygame.display.update()
    clock.tick(60)