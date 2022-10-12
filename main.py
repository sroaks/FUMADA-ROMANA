import pygame
from nave import *
from meteorito import *

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SPQR")
clock = pygame.time.Clock()
"""
"""


             
all_sprites = pygame.sprite.Group()
lista_de_meteoritos = pygame.sprite.Group()
nave = Nave()
all_sprites.add(nave)


GAME_OVER = True
STAY_ALIVE = True
while STAY_ALIVE:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False
            
    all_sprites.update()
    
    fondo = pygame.image.load("recursos/fondo.png").convert()
    screen.blit(fondo, [0, 0])
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

