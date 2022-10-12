import pygame, random
from nave import *
from meteorito import *
from pruebas import *

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SPQR")
clock = pygame.time.Clock()
"""
"""
# ZONA DE DECLARAR IMAGENES


all_sprites = pygame.sprite.Group() # GRUPO PARA LA NAVE
prueba_list = pygame.sprite.Group()
#lista_de_meteoritos = pygame.sprite.Group() # '' / METEORITOS

nave = Nave() # crea la nave para meterla en all_sprites
all_sprites.add(nave)

#meteorito = Meteorito() # crea el meteorito para meterlo en all_sprites
#all_sprites.add(meteorito)

for n in range(5): # iteramos sobre un rango de 5 para crear varios meteoritos
    prueba = Prueba()
    all_sprites.add(prueba)
    prueba_list.add(prueba)

# -----------------------------------------------

GAME_OVER = True
STAY_ALIVE = True
while STAY_ALIVE:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False
    
    #ventana.fill((blanco))
      
    all_sprites.update() # meto all_sprites

    fondo = pygame.image.load("recursos/fondo.png").convert()
    ventana.blit(fondo, [0, 0]) #dibujar muchas imágenes en otra

    all_sprites.draw(ventana) # dibujo all_sprites
  
    #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

    pygame.display.flip()
pygame.quit()

