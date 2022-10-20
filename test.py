import pygame
import random


ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (173,255,47)
amarillo = (255,255,0)
naranja = (255,165,0)
rojo = (255,0,0)
interface_p = (800,90)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(negro)
        self.rect.centerx = 400 # X
        self.rect.centery= 300 # Y
        # A DETERMINAR LA VELOCIDAD
        self.speedx = random.randrange(-1,1)
        self.anchote = 0
        self.largote = 0
           
    def update(self):
        self.rect.centerx += self.speedx
        self.anchote += 10
        self.largote += 10
        self.image = pygame.transform.scale(self.image, (self.anchote, self.largote))
        if self.rect.centerx < -50 or self.rect.centery > ancho + 50 :
            self.rect.centerx = 400 # X
            self.rect.centery= 300 # Y
            self.speedy = random.randrange(-1,1)
            self.anchote = 0
            self.largote = 0