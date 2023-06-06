import pygame
from random import randint
BLACK = (0,0,0)

class Fish(pygame.sprite.Sprite):
    def __init__(self, color, xpos):
        super().__init__()

        width = randint(10, 20)
        height = 10

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0, width, height])

        self.xdir = xpos

        self.rect = self.image.get_rect()

    def update(self):
        self.xdir=randint()
        