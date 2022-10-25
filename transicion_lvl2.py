import pygame, random, sys
from roman_number import *
import sqlite3

pygame.init()
clock = pygame.time.Clock()




def transicion():
    mi_conexion = sqlite3.connect("database/miprimeradb.sqlite3")
    cursor = mi_conexion.cursor()
    cursor.execute("SELECT MAX (ID) , SCORE FROM puntuacion")
    # PARA VER LAS PUNTUACIONES MAS ALTAScursor.execute("SELECT * FROM puntuacion ORDER BY SCORE DESC LIMIT 5")
    puntuachione = cursor.fetchall()

    ancho = 800
    alto = 600
    ventana = pygame.display.set_mode((ancho, 600))
    negro = (0, 0, 0)
    font_2 = pygame.font.SysFont('Bauer', 25)


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
    STAY_ALIVE = True
    while STAY_ALIVE:
        POSI_NAV = (pnvx,pnvy)
        if pnvx <= 200:
            pnvx += 1
        elif pnvy == 550:
            from SEGUNDO_LVL import segundolvl
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


        draw_text("FELICIDADES, HAS PASADO EL PRIMER NIVEL", font_2, (negro), ventana, 50, 50)
        draw_text("id Partida|PUNTUACIÓN",font_2, (negro), ventana, 50, 80)
        draw_text(str(puntuachione),font_2, (negro), ventana, 50, 100)

        pygame.display.flip()
    pygame.quit()