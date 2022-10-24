import pygame, sys, random
from nivel1 import game
 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("SPQR")
ventana = pygame.display.set_mode((500, 500))

pygame.mouse.set_visible(False)
fondo_m = pygame.image.load('recursos/main_menu.png').convert_alpha()
boton1 = pygame.image.load('recursos/boton1.png').convert_alpha()
cursor_img = pygame.image.load('recursos/puntero.png').convert_alpha()
cursor_img_rect = cursor_img.get_rect()
nave_menu = pygame.image.load('recursos/navemenu.png').convert_alpha()
font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def main_menu(): 
    navey = 300 
    click = False
    while True:
        mainClock.tick(30)
        t = pygame.time.get_ticks()//1000
        posi_cursor = pygame.mouse.get_pos()
        if t > 0:
            if navey >= 300:
                navey += 1
            if navey == 325:
                navey = 300
            


        ventana.blit(fondo_m, [0,0])

        mx, my = pygame.mouse.get_pos()
        
        button_1 = ventana.blit(boton1, [155,150])
        if button_1.collidepoint((mx, my)):
            if click:
                game()
    
 
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
            
        ventana.blit(nave_menu,[25,navey])
        ventana.blit(cursor_img, posi_cursor)
        pygame.display.update()

    
 
main_menu()