import pygame, random
import sys
import random
from math import *



pygame.init()
clock = pygame.time.Clock()


def segundolvl():
    pygame.mouse.set_visible(False)
    font_1 = pygame.font.SysFont('Bauer', 20)
    font_2 = pygame.font.SysFont('Bauer', 50)
    risa_sound = pygame.mixer.Sound("recursos/SONIDO/risa.wav")

    def draw_text(text,font,color,ventana,x,y):
        textobj = font.render(text,1,color)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        ventana.blit(textobj,textrect)

    
    w = 800
    h = 600
    ventana = pygame.display.set_mode((w, h))
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
    img_luna = [imgrot1,imgrot2, imgrot3]

    cuore = pygame.image.load("recursos/NAVE_2/cuore.png").convert_alpha()
    cuore = pygame.transform.scale(cuore,(200,200))
    cuore_roto = pygame.image.load("recursos/NAVE_2/cuore_02.png").convert_alpha()
    cuore_roto = pygame.transform.scale(cuore_roto,(200,200))
    corasao = [cuore,cuore_roto]

    img = pygame.image.load("recursos/NAVE_2/cruceta1.png")
    cruceta_2 = pygame.image.load("recursos/NAVE_2/cruceta2.png")

    img1 = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
    img2 = pygame.image.load("recursos/NAVE_2/ENEMI_01_01.png").convert_alpha()
    imgs = [img1,img2]

    class Enemigo:
        def __init__(self):
            self.ancho = 95
            self.alto = 88
            self.x = random.randrange(100,550)
            self.y = 250
            self.speedx = random.randrange(-1,1)/5
            self.speedy = 1/2
    
        def move(self):
            global vida
            self.y += self.speedy
            self.x += self.speedx
            if self.x >= h or self.x <= 0 or self.y >= h:
                if hallegado(self.y):
                    vida -= 10
                    self.reset()
                    
        def show(self,vt):
            self.img = imgs[vt]
                
            return ventana.blit(imgs[vt],[self.x,self.y])
        
        def burst(self):
            global score
            pos = pygame.mouse.get_pos()
            
            if isonEnemi(self.x, self.y, self.ancho, self.alto, pos):
                score += 1
                risa_sound.play()
                self.reset()
                
        def reset(self):
            global score
            self.ancho = 95
            self.alto = 88
            self.x = random.randrange(100,550)
            self.y = 250
            self.speedx = random.randrange(-1,1)/5
            if score > 0 and score < 10:
                self.speedy = 1
            if score >= 10 and score < 20:
                self.speedy = 2
            if score >= 20:
                self.speedy = 2.5

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
        
    enemigos = []
    noenemigos = 5

    for i in range(noenemigos):
        obj = Enemigo()
        enemigos.append(obj)

    def isonEnemi(x, y, ancho, alto, pos):
        if (x < pos[0] < x + ancho) and (y < pos[1] < y + alto):
            return True
        else:
            return False

    def hallegado(y):
        if y >= 525:
            return True
        else:
            return False

    def pointer():
        pos = pygame.mouse.get_pos()
        r = 25
        l = 20
        color = rojo
        for i in range(noenemigos):
            if isonEnemi(enemigos[i].x, enemigos[i].y, enemigos[i].ancho, enemigos[i].alto, pos):
                color = rojo
        pygame.draw.ellipse(ventana, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
        pygame.draw.line(ventana, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
        pygame.draw.line(ventana, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
        pygame.draw.line(ventana, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
        pygame.draw.line(ventana, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4) 

    def close():
        pygame.quit()
        sys.exit()

    
    def game1():
        global vida
        vida = 100
        global score
        score = 0
        global vida_enemigo
        vida_enemigo = 10
        STAY_ALIVE = True
        t = pygame.time.get_ticks()//1000
        t2 = 0
        t3 = 0
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
                        enemigos[i].burst()
                      

            if vida <= 0:
                from derrota_lvl2 import derrota2
                STAY_ALIVE = False
            

            if t2 >= 0 and t2 <= 1:
                draw_text("BIENVENIDO AL SEGUNDO NIVEL",font_2,(blanco), ventana, 120, 150)
            if t2 >= 1 and t2 <= 2:
                draw_text("EL SUEÑO DE TODO PROFESOR...",font_2,(blanco), ventana, 120, 150)
            if t2 >= 2 and t2 <= 3:
                draw_text("PODER MATAR ALUMNOS!!",font_2,(blanco), ventana, 150, 150)

            if t2 >= 3 and score <= 30:
                for i in range(noenemigos):
                    enemigos[i].show(vt)
                for i in range(noenemigos):
                    enemigos[i].move()
            
            if score >= 30:
                if t > 0:
                    t3 += 0.01
                    t3 = round(t3,2)
                if t3 >= 1 and t3 <= 2:
                    draw_text("Parece que nos tenias ganas...",font_2,(blanco), ventana, 120, 150)
                    ventana.blit(corasao[vt],[300,300])
                if t3 >= 2 and t3 <= 4:
                    draw_text("Última Sorpresa!!!!",font_2,(blanco), ventana, 220, 200)
                if t3 >= 4 and vida_enemigo > 0:
                     from tercerlvl import tercerlvl
                     STAY_ALIVE = False
   
                                
            pointer()

            showVida()

            #ventana.blit(img,loc)
            ventana.blit(interior, [0, 0])
            draw_text(str(t2),font_2,(blanco), ventana, 20, 220)
            draw_text(str(score),font_2,(blanco), ventana, 740, 220)
            pygame.display.update()
            clock.tick(60)
    game1()
segundolvl()