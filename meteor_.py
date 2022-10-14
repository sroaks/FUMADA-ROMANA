import random

import pygame

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.angulo = random.randrange(0,359)
        self.rotate_speed = random.randrange(-5,5)
        self.image = pygame.image.load("img/meteorGrey_big4.png").convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = random.randrange(0, 600)
        self.speedy = random.randrange(-1,1)
        self.speedx = random.randrange(-5,-1)
        
    def update(self):
        self.angulo += self.rotate_speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.image = pygame.transform.rotate(pygame.image.load("img/meteorGrey_big4.png").convert_alpha(),self.angulo)


        
  