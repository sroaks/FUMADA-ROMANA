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

    class Enemi(pygame.sprite.Sprite):
        def __init__(self):
            #super().__init__()
            self.image = pygame.image.load("recursos/25.png").convert_alpha()
            self.image.set_colorkey(negro)
            self.rect = self.image.get_rect()
            self.rect.centerx = random.randrange(150,350)
            self.rect.centery = 200
            self.vx = random.randrange(-1,1)
            self.vy = 1

        def update(self,variable_tiempo):
            self.rect.centerx += self.vx/10
            self.rect.centery += self.vy
            self.ancho = self.rect.centerx + 100
            self.alto = self.rect.centery + 170
            self.posicion_enemigo = [self.rect.centerx,self.rect.centery]
            self.superficie_ocupa = [self.rect.centerx,self.rect.centery,self.ancho,self.alto]
            self.variable_tiempo = variable_tiempo
            if self.variable_tiempo == 0:
                self.img = pygame.image.load("recursos/NAVE_2/ENEMI_01_01.png").convert_alpha()
            if self.variable_tiempo == 1:
                self.img = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
            if self.rect.centery > 600 or self.rect.centerx < 0 or self.rect.centerx > 800:
                self.reset()

            return ventana.blit(self.img,self.posicion_enemigo), self.superficie_ocupa
              
        def burst(self):
            pos = pygame.mouse.get_pos()
            if isonEnemi(self.rect.centerx, self.rect.centery, self.ancho, self.alto, pos):
                self.reset()
        
        def reset(self):
            self.rect.centerx = random.randrange(150,350)
            self.rect.centery = 200
            self.vx = random.randrange(-1,1)
            self.vy = 1 
            if self.variable_tiempo == 0:
                self.img = pygame.image.load("recursos/NAVE_2/ENEMI_01_01.png").convert_alpha()
            if self.variable_tiempo == 1:
                self.img = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()

    enemigos = []
    numero_enemigos = random.randrange(1,5) 

    """
    enemi_sprites = pygame.sprite.Group()
    
    """
    for n in range(numero_enemigos):
        enemi = Enemi()
        enemigos.append(enemi)
    
    def isonEnemi(x,y,ancho,alto,pos):
        if (x < pos[0] < x + ancho) and (y < pos[1] < y + alto):
            return True
        else:
            return False
    
    enemigo = Enemi()

    risa_sound = pygame.mixer.Sound("recursos/SONIDO/risa.wav")
    click = False
    score = 0
    t2 = 0
    while STAY_ALIVE:
        clock.tick(60)
        ventana.blit(dungeon, [0, 0])
        t = pygame.time.get_ticks()//1000
        vt = (divmod(t,2)[1])
        if t > 0:
            t2 += 0.01
            t2 = round(t2,2)
        mx, my = pygame.mouse.get_pos()

        posicion_raton = [mx,my]

        if t2 >= 1:
            enemi.update(vt)            
            a, b = enemigo.update(vt)


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
                    if posicion_raton[0] >= b[0] and posicion_raton[0] <= b[2] and posicion_raton[1] >= b[1] and posicion_raton[1] <= b[3]:
                        score += 1
                        risa_sound.play()
                        enemi.burst

    
        ventana.blit(img,loc)
        ventana.blit(interior, [0, 0])
        draw_text(str(t2),font_2,(blanco), ventana, 40, 220)
        draw_text(str(score),font_2,(blanco), ventana, 740, 220)
        pygame.display.flip()
    pygame.quit()
segundolvl()