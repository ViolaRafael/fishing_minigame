import pygame
import time
from paddle import Paddle
from fish import Fish
from random import randint

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("fishgametestthing - fgtt")

paddle = Paddle(WHITE, 30, 10)
paddle.rect.x = 325
paddle.rect.y = 470

fish = Fish(BLUE)
fish.rect.x = 355
fish.rect.y = 470

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle)
all_sprites_list.add(fish)

emJogo = True

clock = pygame.time.Clock()

fishp = 0

while emJogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            emJogo = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
        if paddle.rect.x < 0:
            paddle.rect.x = 0
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
        if paddle.rect.x > 670:
            paddle.rect.x = 670
    
    # https://realpython.com/python-sleep/
    # random.randint(0,680)
    # time.sleep()
    all_sprites_list.update()

    # space for logic to take off fishp

    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(fishp), 1, WHITE)
    screen.blit(text,(605,10))
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()