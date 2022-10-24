import pygame, sys, random


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("SPQR")
ventana = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 35)
negro = (0,0,0)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def intro():
    click = False
    musica = pygame.mixer.Sound("recursos/SONIDO/musicaIntro.wav")
    spqr = pygame.image.load('recursos/INTRO/LOGO.png').convert_alpha()
    spqr.set_colorkey(negro)
    spqr.get_rect()
    sqpr_sxy = 800
    spqr_x = 10

    titulo = pygame.image.load('recursos/INTRO/Título.png').convert_alpha()
    titulo.set_colorkey(negro)
    titulo.get_rect()
    titulo_sxy = 455

    parra = pygame.image.load('recursos/INTRO/Parrafazo.png').convert_alpha()
    parra.set_colorkey(negro)
    parra.get_rect()
    parra_sxy = 650

    while True:
        t = pygame.time.get_ticks() // 1000
        print(t) 
        ventana.fill((negro))
        if click == False and t == 3:
            musica.play(1)
        if t >= 0 and  t < 4:
            draw_text('Hace no mucho tiempo en una galaxia de aquí mismo...', font2, (255, 255, 255), ventana, 50, 250)
        if t > 4 and t < 10:
            sqpr_sxy -= 10
            spqr_x += 5
            spqr = pygame.transform.smoothscale(spqr,(sqpr_sxy,sqpr_sxy))
            ventana.blit(spqr,[spqr_x,0])
        if t >= 8 and t < 40:
            titulo_sxy -= 5
            ventana.blit(titulo,[200,titulo_sxy])
        if t >= 10 and t < 55:
            parra_sxy -= 5
            ventana.blit(parra,[200,parra_sxy])
        if t >= 55:
            from menu import main_menu


        boton1 = pygame.Rect(725, 530, 75, 25)
        pygame.draw.rect(ventana, (255, 0, 0), boton1)
        draw_text('SALTAR', font, (255, 255, 255), ventana, 725, 535)
        mx, my = pygame.mouse.get_pos()
        
        if boton1.collidepoint((mx, my)):
            if click:
                from menu import main_menu
        

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
            
        pygame.display.update()
        mainClock.tick(10)

intro()