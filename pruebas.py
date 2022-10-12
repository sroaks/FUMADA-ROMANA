import pygame, random

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

class Prueba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/METEORITOS/XDV.png").convert_alpha()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect() # Saco la recta de la imagen para definir su posicion
        self.rect.centerx = 750 # X
        self.rect.centery= random.randrange(25, 575) # Y
