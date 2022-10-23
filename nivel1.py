import pygame, random, sys
from tiempop import *
from roman_number import *
from transicion_lvl2 import transicion
import sqlite3

"""
"""
"""
    TO DO LIST:
    - Rotar los meteoritos (hecho, pero hay que ajustarlo) // ok pero debería pulir
    - PROYECTO BARRA DE VIDA, idea : 100 HP, según el meteorito te quita tanto. cuando vida 75% amarillo mitad naranja cuando -de la mitad rojo // ok
    - Base de datos de score
    - Editar los textos cada uno con una fuente color tamaño etc...
    - MENU
    - METER TIMING (QUE EMPIECE DETERMINADOS SEGUNDOS, PARE, SUME METEORITOS, DIFERENTES ENEMIGOS...)
    - diferenciar los sprites para poder darles el timing... meteoritos por un lado otros enemigos por otro etc, asi controlas más
    - DEFINIR WIN // ok
    - LVL 2
    - BASE DE DATOS en este enlace: https://www.youtube.com/watch?v=4FDVzF0Z9Yo&list=WL&index=5&ab_channel=UskoKruM2010
    - METER PAJARRACOS -1 SCORE - 1 VIDA
    - METER HP UP
    - CUANDO FINALIZA TIMING

"""



pygame.init()
clock = pygame.time.Clock()

def game():
    # ----------- BASE DE DATOS --------------------------------
    mi_conexion = sqlite3.connect("database/miprimeradb.sqlite3")
    cursor = mi_conexion.cursor()
    cursor.execute("SELECT max(ID) FROM puntuacion")
    N_PARTIDA = cursor.fetchall()
    N_PARTIDA = list(N_PARTIDA[0])
    N_PARTIDA= (N_PARTIDA[0]+1)
    # ----------- BASE DE DATOS --------------------------------
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
    ventana = pygame.display.set_mode((ancho, 690))
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

    # MI NAVE

    class Nave(pygame.sprite.Sprite): # Clase base simple para objetos de juego visibles.
        def __init__(self): # inicio la clase
            super().__init__() #  superclase sprite
            self.image = pygame.image.load("recursos/nave/NORMAL.png").convert_alpha()
            self.image.set_colorkey(negro) # quitar borde negro
            self.rect = self.image.get_rect() # Saco la recta de la imagen para definir su posicion
            self.rect.centerx = 25 # X
            self.rect.centery = 300 # Y
            self.speed_x = 0 # este pobreto 100pre será 0... (F)
            self.speed_y = 0
            self.sumayup = 0
            self.sumaydw = 0
            self.sumax = 0
            self.vida = 100

        def update(self):
            presiona = pygame.key.get_pressed()
            self.speed_x = 0 # vel X siempre será 0
            self.speed_y = 0 # velocidad Y
            self.contadory = 0 # para darle la aceleración.

            #reponer la imagen estatica
            if presiona != True:
                self.image = pygame.image.load("recursos/nave/NORMAL.png").convert_alpha()   
            # dar movimiento UP
            if presiona[pygame.K_w]:
                self.sumaydw = self.sumaydw*0 # multiplicamos * 0 para resetear (cambio de tecla)
                if self.sumayup <= 40: # este valor lo saqué fijandome en que valor se quedaba presionando 2 sec aprox.
                    self.speed_y = -2
                    self.contadory = 1 # contador
                    self.image = pygame.image.load("recursos/nave/subir.png").convert_alpha() 
                if self.sumayup > 40: 
                    self.speed_y = -5
                    self.image = pygame.image.load("recursos/nave/subir fuerte.png").convert_alpha() #por fin doy uso a mi tan preciada imagen.

            # dar movimiento DOWN   
            if presiona[pygame.K_s]:
                self.sumayup = self.sumayup*0
                if self.sumaydw <= 40:  
                    self.speed_y = 2
                    self.contadory = 1
                    self.image = pygame.image.load("recursos/nave/bajar.png").convert_alpha()
                if self.sumaydw > 40:
                    self.speed_y = 5
                    self.image = pygame.image.load("recursos/nave/bajar fuerte.png").convert_alpha()

            self.sumayup += self.contadory
            self.sumaydw += self.contadory
            self.rect.y += self.speed_y
            #posicion inicial nave
            if self.rect.bottom > alto:
                self.rect.bottom = alto
            if self.rect.bottom < 50:
                self.rect.bottom = 50

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)


    # METEORITOS

    class Meteoritos(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.angulo = random.randrange(0,359)
            self.rotate_speed = random.randrange(-1,1)
            self.image = pygame.image.load("recursos/METEORITOS/CCC.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.image.set_colorkey(negro)
            self.rect.centerx = 750 # X
            self.rect.centery= random.randrange(25, 575) # Y
            # A DETERMINAR LA VELOCIDAD
            self.speedy = random.randrange(-1,1)
            self.speedx = random.randrange(-5,-1)
            # seleccionar meteorito aleatorio
            self.image = random.choice(meteoritos_imagenes)
            
        def update(self):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
            #metiendo rotachione a los meteoritos
            self.angulo += self.rotate_speed #POR FIIIIIIIIIIIIIIIIIIIIIN !!!!!
            #self.image = pygame.transform.rotate(random.choice(meteoritos_imagenes),self.angulo).convert_alpha()
            if self.rect.centery < -50 or self.rect.centerx < -50 or self.rect.centery > ancho + 50 : 
                self.rect.centerx = 750 # X
                self.rect.centery= random.randrange(25, 575)
                self.speedx = random.randrange(-10, -5)
                self.speedy = random.randrange(-1,1)


    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("recursos/nave/balazo_lokete.png")
            self.image.set_colorkey(negro)
            self.rect = self.image.get_rect()
            self.rect.y = y
            self.rect.centerx = x
            self.speedx = 10

        def update(self):
            self.rect.x += self.speedx
            if self.rect.x > 800:
                self.kill() #esto hace desaparecer el balazo del tiron

    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center):
            super().__init__()
            self.image = explosion_anim[0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50 # velocidad explosion

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim):
                    self.kill() 
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    # ZONA DE DECLARAR IMAGENES

    meteoritos_imagenes=[]
    lista_de_meteoritos=["recursos/METEORITOS/CCC.png","recursos/METEORITOS/I.png","recursos/METEORITOS/IV.png","recursos/METEORITOS/L.png","recursos/METEORITOS/MIX.png","recursos/METEORITOS/XDV.png"]
    for img in lista_de_meteoritos:
        meteoritos_imagenes.append(pygame.image.load(img).convert_alpha())

    fondo = pygame.image.load("recursos/fondo.png").convert_alpha()
    fondo_02 = pygame.image.load("recursos/fono_02.png").convert_alpha()
    interface = pygame.image.load("recursos/f_interface.png").convert_alpha()
    img_vida = pygame.image.load("recursos/100.png").convert_alpha()
    coliseo = pygame.image.load("recursos/COLISEO.png").convert_alpha()
    

    explosion_anim = []
    for i in range(7):
        file = "recursos/explosion/EXP0{}.png".format(i)
        img = pygame.image.load(file).convert_alpha()
        img.set_colorkey(negro)
        img_scale = pygame.transform.scale(img, (70, 70))
        explosion_anim.append(img_scale)

    # ---------- metiendo clima -----------------------

    POSI_C = (275,610)
    POSI_BRUJ = (200, 600)
    POSI_GRADOS = (600,15)
    # import de la API : clima
    clima = tiempo


    img_clima = pygame.image.load("recursos/efectos_clima/nube01.png").convert_alpha()
    img_brujula_v = pygame.image.load("recursos/efectos_clima/brújula.png").convert_alpha()

    imgl = []
    if tiempo == "Clear":
        for w in range(3):
            file = 'recursos/efectos_clima/sol0{}.png'.format(w)
            img = pygame.image.load(file).convert_alpha()
            img.set_colorkey(negro)
            #img_scale = pygame.transform.scale(img, (70, 70))
            imgl.append(img)
    if tiempo == "Clouds":
        for w in range(3):
            file = 'recursos/efectos_clima/nube0{}.png'.format(w)
            img = pygame.image.load(file).convert_alpha()
            img.set_colorkey(negro)
            #img_scale = pygame.transform.scale(img, (70, 70))
            imgl.append(img)
    if tiempo == "Rain":
        for w in range(3):
            file = 'recursos/efectos_clima/rain0{}.png'.format(w)
            img = pygame.image.load(file).convert_alpha()
            img.set_colorkey(negro)
            #img_scale = pygame.transform.scale(img, (70, 70))
            imgl.append(img)
    
    # -----------------------------------------------------


    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    lista_de_meteoritos = pygame.sprite.Group()

    nave = Nave()

    all_sprites.add(nave)

    for n in range(3):
        meteoritos=Meteoritos()
        all_sprites.add(meteoritos)
        lista_de_meteoritos.add(meteoritos)


    cielo = pygame.image.load("recursos/cielo.png").convert_alpha()
    GAME_OVER = True
    STAY_ALIVE = True
    fx = 0
    aux = 1 # variable para tiempo numero entero
    """
    Trae de la base de datos, el registro más alto y sumale 1
    N_PARTIDA = [00000]
    """
    t = pygame.time.get_ticks()//1000
    t2 = 0
    while STAY_ALIVE:
        ventana.blit(cielo, [0,0])
        if t > 0:
            t2 += 0.01
            t2 = round(t2,2)
        
        if aux == t2:
            aux += 1
            x = list(divmod(t2,3))
            if x[1] == 1:
                img_clima= imgl[0]
                fx -= 3
            if x[1] == 2:
                img_clima= imgl[1]
                fx -= 3
            if x[1] == 0:
                img_clima= imgl[2]
                fx -= 3
        
        
        ventana.blit(fondo_02, [fx, 0])
        # ROTACIÓN BRUJULA SEGUN GRADOS API
       
        if GAME_OVER:
            
            GAME_OVER = False
            
            score = 0
            nave.vida = 100
            disparos = 0
            acuraci = 0
            score_tt = 0

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                STAY_ALIVE = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    disparos += 1
                    nave.shoot()
                  
        all_sprites.update()
        # Colisiones disparos
        hits = pygame.sprite.groupcollide(lista_de_meteoritos, bullets, True, True)
        for hit in hits:
            score += 1
            explosion = Explosion(hit.rect.center)
            all_sprites.add(explosion)
            meteor = Meteoritos()
            all_sprites.add(meteor)
            lista_de_meteoritos.add(meteor)
            
        # Colisiones jugador - meteoro
        marcador = []
        hits = pygame.sprite.spritecollide(nave, lista_de_meteoritos, True)
        if hits:
            nave.vida -= 25
            meteor = Meteoritos()
            all_sprites.add(meteor)
            lista_de_meteoritos.add(meteor)
            if nave.vida >= 100:
                img_vida = pygame.image.load("recursos/100.png").convert_alpha()
            elif nave.vida == 75:
                img_vida = pygame.image.load("recursos/75.png").convert_alpha()
            elif nave.vida == 50:
                img_vida = pygame.image.load("recursos/50.png").convert_alpha()
            elif nave.vida == 25:
                img_vida = pygame.image.load("recursos/25.png").convert_alpha()
            else:
                STAY_ALIVE = False
        if t2 == 60 and score < 30:
            STAY_ALIVE = False
        if score == 10:
            score_tt = nave.vida+acuraci-t2
            marcador.append(N_PARTIDA)
            marcador.append(t2)
            marcador.append(acuraci)
            marcador.append(nave.vida)
            marcador.append(round(score_tt,2))
            marcador = tuple(marcador)
            print(marcador)
            
            cursor.execute("INSERT INTO puntuacion VALUES "\
                "{}".format(marcador))
            mi_conexion.commit()
            mi_conexion.close()
            
            transicion()

        # SCORE N_ROMAN

        N=score
        N = roman_number(N)

        if disparos > 0 and score > 0:
            acuraci = round((score/disparos)*100 , 2)

        
        ventana.blit(fondo, [0, 0])
        ventana.blit(coliseo, [fx+800, 500])
        ventana.blit(interface, [0,585])

        img_vida = pygame.transform.scale(img_vida, (158, 18))
        ventana.blit(img_vida, [19,614])

        all_sprites.draw(ventana)

        ventana.blit(img_clima,POSI_C)
        ventana.blit(pygame.transform.rotate(img_brujula_v,grados_viento),POSI_BRUJ)

        draw_text(str(N), font_2, (amarillo), ventana, 375, 620)
        draw_text('PRECISIÓN:', font_2, (amarillo), ventana, 455, 610)
        draw_text(str(acuraci)+'%', font_2, (amarillo), ventana, 570, 612)
        draw_text(str(t2),font_2,(amarillo), ventana, 19, 650)
        draw_text('Vel-viento m/s:',font_2,(amarillo),ventana,51,640)
        draw_text(str(velocidad_viento),font_2,(amarillo),ventana,145,660)
        draw_text('0º', font_3, (amarillo), ventana, 230, 605)
        draw_text('90º', font_3, (amarillo), ventana, 260, 632)
        draw_text('180º', font_3, (amarillo), ventana, 230, 665)
        draw_text('270º', font_3, (amarillo), ventana, 195, 632)
    
        #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

        pygame.display.flip()
    pygame.quit()