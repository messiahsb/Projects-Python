import pygame
import sys

# init pygame
pygame.init()

WIN_HEIGHT = 800 
WIN_WIDTH = 800
WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))

pygame.display.set_caption("PyPong")

clock = pygame.time.Clock()
running = True

ball_x = WIN_HEIGHT/2
ball_y = WIN_WIDTH/2
ball_radius = 10
ball_speed_x = 0
ball_speed_y = 0


while running:

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_speed_x = 3
            elif event.key == pygame.K_LEFT:
                ball_speed_x = -3
            if event.key == pygame.K_UP:
                ball_speed_y = -3
            elif event.key == pygame.K_DOWN:
                ball_speed_y = 3

    # Update Positions
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    

    # Drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius) 
    

    pygame.display.update()
    clock.tick(60)