import pygame, random
from tiempop import tiempo, v_viento
#from crono import *

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
clock = pygame.time.Clock()

class Clima(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/efectos_clima/.sol_1png").convert_alpha()
        self.image.set_colorkey(negro) # quitar borde negro
        self.rect = self.image.get_rect() # Saco la recta de la imagen para definir su posicion
        self.rect.centerx = 650 # X
        self.rect.centery = 50 # Y
        
    def dibuajar(self):
        clear_imagenes[0]
        clear_imagenes[1]
        clear_imagenes[2]



clear_imagenes=[]
lista_de_clear=["recursos/efectos_clima/sol_1.png","recursos/efectos_clima/sol_2.png","recursos/efectos_clima/sol_3.png",]
for img in lista_de_clear:
    clear_imagenes(pygame.image.load(img).convert_alpha())



fondo = pygame.image.load("recursos/fondo.png").convert()

GAME_OVER = True
STAY_ALIVE = True
while STAY_ALIVE:
    
    if GAME_OVER:
        
        GAME_OVER = False
        all_sprites = pygame.sprite.Group()
        clima = Clima()
        all_sprites.add(clima)
        score = 0

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False

    all_sprites.update()
    
    ventana.fill(blanco)
    
    all_sprites.draw(ventana)
  
    #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

    pygame.display.flip()
pygame.quit()