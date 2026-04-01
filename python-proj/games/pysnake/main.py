import pygame
import sys
from pygame.math import Vector2
import random

pygame.init()


CELL_SIZE = 30
NUMBER_CELLS = 25
WIN_HEIGHT = WIN_WIDTH = CELL_SIZE*NUMBER_CELLS
OFFSET = 75 


screen = pygame.display.set_mode((2*OFFSET + WIN_WIDTH, 2*OFFSET + WIN_HEIGHT))
clock = pygame.time.Clock()
title_font = pygame.font.Font(None, 60)
score_font  = pygame.font.Font(None, 40)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 52, 24)

class Food():
    def __init__(self, snake):
        self.position = self.gen_new_pos(snake)

    def draw(self):
        food_rect = pygame.Rect(OFFSET+self.position.x*CELL_SIZE, OFFSET+self.position.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
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
            seg_rect = (OFFSET+seg.x * CELL_SIZE, OFFSET+seg.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, DARK_GREEN, seg_rect, 0, 7)
   
    def move_snake(self, dir):
        self.direction = dir
    
    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)


    def grow_body(self):
            self.body.append(self.body[0])

class Game():
    def __init__(self):
        self.snake = Snake()        
        self.food = Food(self.snake.body)
        self.running = True
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        if self.running:
            self.eat_tail()
            self.check_eat()
            self.check_wall()
            self.snake.update()

    def check_eat(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.gen_new_pos(self.snake.body)   
            self.snake.grow_body()
            self.score +=1 

    def check_wall(self):
        if self.snake.body[0].x == NUMBER_CELLS or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == NUMBER_CELLS or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.running = False
        self.score = 0

    def eat_tail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

game = Game()
snake = game.snake
food = game.food
running = True

while running:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE: 
                if game.running:
                    game.update()
                    # running = False
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
    pygame.draw.rect(screen, DARK_GREEN, 
                     (OFFSET-5, OFFSET-5, CELL_SIZE*NUMBER_CELLS+10, CELL_SIZE*NUMBER_CELLS+10), 5)
    game.draw()
    title_surface = title_font.render("Retro Snake", True, DARK_GREEN)
    screen.blit(title_surface, (OFFSET-5, 20))
    score_surface = score_font.render(str(game.score), True, DARK_GREEN)
    screen.blit(score_surface, (OFFSET-5, OFFSET+CELL_SIZE*NUMBER_CELLS+10))

    pygame.display.update()
    clock.tick(60)