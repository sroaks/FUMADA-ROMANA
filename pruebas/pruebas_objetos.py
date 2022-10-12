import pygame

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

class Nave(pygame.sprite.Sprite): # Clase base simple para objetos de juego visibles.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/nave/NORMAL.png").convert_alpha()
        self.image.set_colorkey(negro) # quitar borde negro
        self.rect = self.image.get_rect() # Saco la recta de la imagen para definir su posicion
        self.rect.centery = 10
        self.rect.bottom = 300
        self.speed_x = 0
        self.vida = 100