import pygame
import sys
import random

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
    def __init__(self): 
        self.y = WIN_HEIGHT/2
        self.x = WIN_WIDTH/2
        self.radius = 10
        self.x_velocity = 6
        self.y_velocity = 6
        self.hitbox  = pygame.Rect(0,0,10,10)
        self.hitbox.center =(self.x, self.y)

    def moveBall(self, human, cpu):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.hitbox.center = (self.x, self.y)

        if self.hitbox.bottom >= WIN_HEIGHT or self.hitbox.top <= 0:
            self.y_velocity *= -1

        if self.hitbox.right >= WIN_WIDTH :
            self.x_velocity *= -1
            update_points(0)
        elif self.hitbox.left <= 0:
            self.x_velocity *= -1
            update_points(1)
        if self.hitbox.colliderect(human) or self.hitbox.colliderect(cpu):
            self.x_velocity *= -1

    def reset_ball(self):

        self.x = WIN_WIDTH/2 - 10
        self.y = random.randint(10, 100)
        self.y_velocity *= random.choice([-1,1])
        self.x_velocity *= random.choice([-1,1])

class Paddle():
    def __init__(self, x, y):
        self.paddle  = pygame.Rect(0,0,20,100)
        self.x = x
        self.y = y
        self.velocity = 0
        self.paddle.center = (self.x, self.y)
    
    def movePaddle(self):
        player.y += player.velocity
        player.paddle.center = (player.x, player.y)
        if player.paddle.top <= 0:
            self.paddle.top = 0
        if player.paddle.bottom >= WIN_HEIGHT:
            self.paddle.bottom = WIN_HEIGHT
     
cpu_paddle = Paddle(30, WIN_HEIGHT/2) 
cpu_paddle.velocity = 6
player = Paddle(WIN_WIDTH-30, WIN_HEIGHT/2) 
ball =  Ball()

cpu_points = 0
player_points = 0
def update_points(i):
    global cpu_points, player_points
    if i:
        cpu_points+=1
        ball.reset_ball()
    else:
        player_points+=1
        ball.reset_ball()


def moveCPU():
    cpu_paddle.paddle.y += cpu_paddle.velocity
    if ball.hitbox.centery >= cpu_paddle.paddle.centery:
        cpu_paddle.velocity = 6
    if ball.hitbox.centery <= cpu_paddle.paddle.centery:
        cpu_paddle.velocity = -6

    if cpu_paddle.paddle.top <= 0:
        cpu_paddle.paddle.top = 0
    if cpu_paddle.paddle.bottom >= WIN_HEIGHT:
        cpu_paddle.paddle.bottom = WIN_HEIGHT



score_font = pygame.font.Font(None, 100)
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity = -6
            elif event.key == pygame.K_DOWN:
                player.velocity = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.velocity = 0
            elif event.key == pygame.K_DOWN:
                player.velocity = 0
   
    # Update Positions
    ball.moveBall(player.paddle, cpu_paddle.paddle)
    player.movePaddle()
    moveCPU()
    

    # Drawing
    screen.fill(BLACK)

    cpu_score_surface = score_font.render(str(cpu_points), True, WHITE)
    player_score_surface = score_font.render(str(player_points), True, WHITE)
    screen.blit(cpu_score_surface, (WIN_WIDTH/4, 20))
    screen.blit(player_score_surface, (3*WIN_WIDTH/4, 20))

    for y in range(10, WIN_HEIGHT, 40):
      pygame.draw.aaline(screen, WHITE, (WIN_WIDTH/2, y), (WIN_WIDTH/2, y + 20))
    pygame.draw.rect(screen, WHITE, cpu_paddle.paddle)
    pygame.draw.rect(screen, WHITE, player.paddle)
    pygame.draw.ellipse(screen, WHITE, ball.hitbox) 



    pygame.display.update()
    clock.tick(60)

