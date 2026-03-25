import pygame
import sys

# init pygame
pygame.init()

WIN_HEIGHT = 800 
WIN_WIDTH = 1280
WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("PyPong")

clock = pygame.time.Clock()
running = True

class Ball():
    ball_y = WIN_HEIGHT/2
    ball_x = WIN_WIDTH/2
    ball_radius = 10
    ball_speed_x = 0
    ball_speed_y = 0
    hitbox  = pygame.Rect(0,0,10,10)
    hitbox.center =(ball_x, ball_y)

class Paddle():
    paddle  = pygame.Rect(0,0,20,100)
    paddle_y = WIN_HEIGHT/2
    paddle_x = 30

    def set_center(self):
        self.paddle.center = (self.paddle_x, self.paddle_y)

cpu_paddle = Paddle() 
player = Paddle() 
player.paddle.centerx = WIN_WIDTH-30
player.set_center()

ball =  Ball()

while running:

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_RIGHT:
    #             ball_speed_x = 3
    #         elif event.key == pygame.K_LEFT:
    #             ball_speed_x = -3
    #         if event.key == pygame.K_UP:
    #             ball_speed_y = -3
    #         elif event.key == pygame.K_DOWN:
    #             ball_speed_y = 3

    # # Update Positions
    # ball_x += ball_speed_x
    # ball_y += ball_speed_y
    

    # Drawing
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball.hitbox) 
    pygame.draw.rect(screen, WHITE, cpu_paddle.paddle)
    pygame.draw.rect(screen, WHITE, player.paddle)

    pygame.display.update()
    clock.tick(60)