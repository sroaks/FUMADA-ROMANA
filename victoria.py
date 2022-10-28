import pygame, sys, random

 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("SPQR")
ventana = pygame.display.set_mode((500, 500))

blanco = (255, 255, 255)
negro = (0,0,0)
verde = (173,255,47)
amarillo = (255,255,0)
naranja = (255,165,0)
rojo = (255,0,0)

pygame.mouse.set_visible(False)
cielo = pygame.image.load('recursos/cielo.png').convert_alpha()
victoria = pygame.image.load('recursos/vistoria.png').convert_alpha()
boton1 = pygame.image.load('recursos/boton1.png').convert_alpha()
cursor_img = pygame.image.load('recursos/puntero.png').convert_alpha()
cursor_img_rect = cursor_img.get_rect()
font = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def victoria1(): 
    click = False
    while True:
        ventana.blit(cielo,[0,0])  

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        ventana.blit(victoria,[75,75])
        draw_text("GRACIAS POR TODO!!",font,(negro), ventana, 80, 400)
        draw_text("Gonzalo Robles <3",font2,(negro), ventana, 300, 480)
        pygame.display.update()

victoria1()