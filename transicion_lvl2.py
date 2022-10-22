import pygame, random, sys

from roman_number import *

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (173,255,47)
amarillo = (255,255,0)
naranja = (255,165,0)
rojo = (255,0,0)
interface_p = (800,90)

pygame.init()
ventana = pygame.display.set_mode((ancho, 600))
pygame.display.set_caption("SPQR")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 15)
font_2 = pygame.font.SysFont('Bauer', 25)
font_3 = pygame.font.SysFont('Bauer', 13)

def draw_text(text,font,color,ventana,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    ventana.blit(textobj,textrect)

cielo = pygame.image.load("recursos/cielo.png").convert_alpha()
coliseo = pygame.image.load("recursos/COLISEO_transi.png").convert_alpha()
coliseo_door = pygame.image.load("recursos/COLISEO_transi_open.png").convert_alpha()
nave_transi = pygame.image.load("recursos/nave/subir fuerte.png").convert_alpha()
pnvx = 25
pnvy = 300
pcolix = 550
pcoliy = 10

GAME_OVER = True
STAY_ALIVE = True

while STAY_ALIVE:
    POSI_NAV = (pnvx,pnvy)
    if pnvx <= 200:
        pnvx += 1
    elif pnvy == 550:
        from SEGUNDO_LVL import *
    else:
        pnvx += 2
        pnvy += 1


    ventana.blit(cielo, [0,0])
    if pcolix > 350:
        pcolix -= 1
        ventana.blit(coliseo,[pcolix,pcoliy])
    else:
        ventana.blit(coliseo_door,[pcolix,pcoliy])

    ventana.blit(nave_transi,POSI_NAV)
    

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False

    """
    Te traes de la BASES , los datos del registro más alto (que será el último y el de esta partida)
    draw_text("str(marcador)", font_2, (amarillo), ventana, 375, 620)
    """

    draw_text("FELICIDADES, HAS PASADO EL PRIMER NIVEL", font_2, (negro), ventana, 50, 50)

    pygame.display.flip()
pygame.quit()