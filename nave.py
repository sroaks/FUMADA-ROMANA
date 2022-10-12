import pygame

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)
"""
"""

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/nave/NORMAL.png").convert_alpha()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.centery = 10
        self.rect.bottom = 300
        self.speed_x = 0
        self.vida = 100
    def update(self):
        presiona = pygame.key.get_pressed()
        mantiene = 0
        self.speed_y = 0
        if presiona != True or mantiene != True:
             self.image = pygame.image.load("recursos/nave/NORMAL.png").convert_alpha()            
        if presiona[pygame.K_w]:
            self.speed_y = -10
            self.image = pygame.image.load("recursos/nave/subir.png").convert_alpha()
        """
        Quiero que cuando se mantenga pulsado acelere y cambia img
        if mantiene[pygame.K_w]:
            self.speed_y = -5
            self.image = pygame.image.load("recursos/nave/subir fuerte.png").convert_alpha()
            
        """
        if presiona[pygame.K_s]:
            self.speed_y = 10
            self.image = pygame.image.load("recursos/nave/bajar.png").convert_alpha()
        self.rect.y += self.speed_y
        if self.rect.bottom > alto:
            self.rect.bottom = alto
        if self.rect.bottom < 50:
            self.rect.bottom = 50