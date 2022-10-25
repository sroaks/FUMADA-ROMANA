import pygame, random


pygame.init()
clock = pygame.time.Clock()


def segundolvl():
    
    
    pygame.mouse.set_visible(False)
    t = pygame.time.get_ticks()
    font_2 = pygame.font.SysFont('Bauer', 50)

    def draw_text(text,font,color,ventana,x,y):
        textobj = font.render(text,1,color)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        ventana.blit(textobj,textrect)

    
    ancho = 800
    alto = 600
    ventana = pygame.display.set_mode((ancho, alto))
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    verde = (173,255,47)
    amarillo = (255,255,0)
    naranja = (255,165,0)
    rojo = (255,0,0)
    interface_p = (800,90)
    POSI_C = (400,300)
    STAY_ALIVE = True

    dungeon = pygame.image.load("recursos/NAVE_2/dungeon.png")
    interior = pygame.image.load("recursos/NAVE_2/interior nave.png")
    img = pygame.image.load("recursos/NAVE_2/cruceta1.png")
    cruceta_2 = pygame.image.load("recursos/NAVE_2/cruceta2.png")
    pictue=pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()

    class Enemigo(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.image.set_colorkey(blanco)
            self.rect.centerx = random.randrange(250,400) # X
            self.rect.centery= 300 # Y
            self.speedx = 1
            self.speedy = 1
            self.anchote = 20
            self.largote = 24
            
        def update(self):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
            self.anchote += 10
            self.largote += (self.anchote * 1.2)
            #self.image = pygame.transform.scale(self.image, (self.anchote, self.largote))
            if self.rect.centerx < 0 or self.rect.centery > ancho + 10 or self.rect.centery > 650:
                self.rect.centerx = 400 # X
                self.rect.centery= 300 # Y
                self.speedx = random.randrange(-1,1)
                self.speedy = 1
                self.anchote = 0
                self.largote = 0
    enemigo_sprites = pygame.sprite.Group()
    enemigo = Enemigo()
    enemigo_sprites.add(enemigo)

    t = pygame.time.get_ticks()//1000
    q3 = 0
    while STAY_ALIVE:
        clock.tick(10)
        if t > 0:
            q3 += 1/10
            q3 = round(q3,1)
        
        ventana.blit(dungeon, [0, 0])
        picturet = pygame.transform.scale(pictue, (20,24))
        
        mx, my = pygame.mouse.get_pos()
        rot = 0
        loc = [mx-40, my-40]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                STAY_ALIVE = False     
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                if click == True and pygame.mouse.get_pressed() == (1, 0, 0):
                    img = cruceta_2
                    ventana.blit(img, (loc))
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
                if click == False:
                    img = pygame.image.load("recursos/NAVE_2/cruceta1.png")

        
        
        #all_sprites.update()

        
        enemigo_sprites.update()
        if q3 >= 5:
            enemigo_sprites.draw(ventana)
        ventana.blit(pygame.transform.rotate(img, rot), (loc))
        

        """
        
        ventana.blit(picturet, POSI_C)
        """

        """

        N=score
        N = roman_number(N)

        if disparos >0 and score >0:
            acuraci = round((score/disparos)*100 , 2)

        
        ventana.blit(fondo, [0, 0])
        ventana.blit(interface, [0,585])

        img_vida = pygame.transform.scale(img_vida, (158, 18))
        ventana.blit(img_vida, [19,614])

        all_sprites.draw(ventana)

        ventana.blit(img_clima,POSI_C)
        ventana.blit(img_grados_v, POSI_GRADOS)
        ventana.blit(pygame.transform.rotate(img_brujula_v,grados_viento),POSI_BRUJ)

        draw_text(str(N), font_2, (amarillo), ventana, 375, 620)
        draw_text(str(acuraci)+'%', font_2, (amarillo), ventana, 500, 620)
        draw_text(str(t),font_2,(amarillo), ventana, 19, 650)
        draw_text('Vel-viento m/s:',font,(rojo),ventana,450,10)
        draw_text(str(velocidad_viento),font,(rojo),ventana,545,10)
        """
        
        ventana.blit(interior, [0, 0])
        draw_text(str(q3),font_2,(blanco), ventana, 40, 220)
        pygame.display.flip()
    pygame.quit()
segundolvl()