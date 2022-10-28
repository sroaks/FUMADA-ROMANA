import pygame, random
import sys
import random
from math import *


pygame.init()
clock = pygame.time.Clock()

def tercerlvl():
    pygame.mouse.set_visible(False)
    font_1 = pygame.font.SysFont('Bauer', 20)
    font_2 = pygame.font.SysFont('Bauer', 50)

    def draw_text(text,font,color,ventana,x,y):
        textobj = font.render(text,1,color)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        ventana.blit(textobj,textrect)

    w = 800
    h = 600
    ventana = pygame.display.set_mode((w, h))
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    verde = (173,255,47)
    amarillo = (255,255,0)
    naranja = (255,165,0)
    rojo = (255,0,0)

    dungeon = pygame.image.load("recursos/NAVE_2/dungeon.png")
    interior = pygame.image.load("recursos/NAVE_2/interior nave.png")
    imgrot1 = pygame.image.load("recursos/NAVE_2/rompiento_01.png").convert_alpha()
    imgrot2 = pygame.image.load("recursos/NAVE_2/rompiendo_02.png").convert_alpha()
    imgrot3 = pygame.image.load("recursos/NAVE_2/rompiendo_03.png").convert_alpha()

    img = pygame.image.load("recursos/NAVE_2/cruceta1.png")
    cruceta_2 = pygame.image.load("recursos/NAVE_2/cruceta2.png")

    class Udemy():
        def __init__(self):
            self.ancho = 400
            self.alto = 150
            self.x = 100
            self.y = 150
            self.speedx = 0
            self.speedy = 1

        def move(self):
            global vida
            self.y += self.speedy
            self.x += self.speedx
            if hallegado(self.y):
                vida -= 100

        def show(self,vt):
            if vt == 0:
                self.ancho += 1
                self.alto += 0.5
            if vt == 1:
                self.ancho += 1
                self.alto += 0.5
            self.img = pygame.image.load("recursos/NAVE_2/boss_final_400x150.png").convert_alpha()
            self.img = pygame.transform.scale(self.img,(self.ancho,self.alto))
            return ventana.blit(self.img,[self.x,self.y])
        
        def burst(self):
            global vida_enemigo
            pos = pygame.mouse.get_pos()
            
            if isonEnemi(self.x, self.y, self.ancho, self.alto, pos):
                vida_enemigo -= 25

    udemy=[]
    
    noenemigos = 1
    

    for i in range(noenemigos):
        enemigo = Udemy()
        udemy.append(enemigo)

    def showVida():
        img_luna = [imgrot1,imgrot2, imgrot3]
        color = verde
        if vida > 75:
            color = verde
        if vida < 75 and vida > 50:
            color = amarillo
            img_luna = img_luna[0]
            ventana.blit(img_luna,[0,0])
        if vida < 50 and vida > 25:
            color = naranja
            img_luna = img_luna[1]
            ventana.blit(img_luna,[0,0])
        if vida < 25:
            color = rojo
            img_luna = img_luna[2]
            ventana.blit(img_luna,[0,0])
        scoreText = font_1.render("HP: " + str(vida), True, color)
        ventana.blit(scoreText, (10,310))
        pygame.draw.rect(ventana,(color),(0,330,vida,20))
    
    def showVida_enemigo():
        color = rojo
        pygame.draw.rect(ventana,(color),(150,130,vida_enemigo,10))

    def isonEnemi(x, y, ancho, alto, pos):
        if (x < pos[0] < x + ancho) and (y < pos[1] < y + alto):
            return True
        else:
            return False
    
    def hallegado(y):
        if y == 400:
            return True
        else:
            return False
    
    def pointer():
        pos = pygame.mouse.get_pos()
        r = 25
        l = 20
        color = rojo
        for i in range(noenemigos):
            if isonEnemi(udemy[i].x, udemy[i].y, udemy[i].ancho, udemy[i].alto, pos):
                color = rojo
        pygame.draw.ellipse(ventana, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
        pygame.draw.line(ventana, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
        pygame.draw.line(ventana, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
        pygame.draw.line(ventana, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
        pygame.draw.line(ventana, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4) 

    def close():
        pygame.quit()
        sys.exit()

    def game2():
        global vida
        vida = 100
        global vida_enemigo
        vida_enemigo = 300
        STAY_ALIVE = True
        t = pygame.time.get_ticks()//1000
        t2 = 0
        while STAY_ALIVE:
            ventana.blit(dungeon, [0, 0])
            t = pygame.time.get_ticks()//1000
            if t > 0:
                t2 += 0.01
                t2 = round(t2,2)

            vt = (divmod(t,2)[1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(noenemigos):
                        udemy[i].burst()
                    
                    
            if vida == 0:
                from derrota_lvl2 import derrota2
                STAY_ALIVE = False
                
            
            if vida_enemigo == 0:
                from victoria import victoria1
                STAY_ALIVE = False
                
            

            if t2 >= 0 and vida_enemigo > 0:
                for i in range(noenemigos):
                    udemy[i].show(vt)
                for i in range(noenemigos):
                    udemy[i].move()

            pointer()

            showVida()
            showVida_enemigo()

            #ventana.blit(img,loc)
            ventana.blit(interior, [0, 0])
            draw_text(str(t2),font_2,(blanco), ventana, 20, 220)
            draw_text(str(vida_enemigo),font_2,(blanco), ventana, 740, 220)
            pygame.display.update()
            clock.tick(60)
    game2()
tercerlvl()