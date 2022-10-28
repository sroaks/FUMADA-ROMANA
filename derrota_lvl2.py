import pygame, sys, random

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("SPQR")
ventana = pygame.display.set_mode((500, 500))
blanco = (255, 255, 255)
negro = (0, 0, 0)
pygame.mouse.set_visible(False)
fondo_m = pygame.image.load('recursos/main_menu.png').convert_alpha()
derrota = pygame.image.load('recursos/derrota.png').convert_alpha()
boton1 = pygame.image.load('recursos/boton1.png').convert_alpha()
cursor_img = pygame.image.load('recursos/puntero.png').convert_alpha()
cursor_img_rect = cursor_img.get_rect()
nave_menu = pygame.image.load('recursos/navemenu.png').convert_alpha()
blanco = (255, 255, 255)
font = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 40)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def derrota2():
    STAY_ALIVE = True
    click = False
    while STAY_ALIVE:
        mainClock.tick(30)
        posi_cursor = pygame.mouse.get_pos()

        ventana.blit(fondo_m, [0,0])
        mx, my = pygame.mouse.get_pos()
        
        button_1 = ventana.blit(boton1, [155,250])
        if button_1.collidepoint((mx, my)):
            if click:
                from SEGUNDO_LVL import segundolvl
                STAY_ALIVE = False

        boton2 = pygame.draw.rect(ventana,blanco,(175,330,150,50))
        if boton2.collidepoint((mx, my)):
            if click:
                pygame.quit()

 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        draw_text("YOU LOSE",font,(blanco),ventana,160,150)
        draw_text("ME RINDO",font2,(negro),ventana,180,340)
        ventana.blit(cursor_img, posi_cursor)
        pygame.display.update()
derrota2()