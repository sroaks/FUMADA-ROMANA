from asyncio import events
import pygame
import sys


ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (173,255,47)
amarillo = (255,255,0)
naranja = (255,165,0)
rojo = (255,0,0)

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SPQR")



while True:
    Tiempo = pygame.time.get_ticks()/1000
    print (Tiempo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys:exit()

    pygame.display.update()