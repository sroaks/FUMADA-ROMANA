import pygame, random

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (173,255,47)
amarillo = (255,255,0)
naranja = (255,165,0)
rojo = (255,0,0)

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SPQR")
clock = pygame.time.Clock()
"""
"""
"""
TO DO LIST:
- Mantener presionado
- Rotar los meteoritos
- PROYECTO BARRA DE VIDA, idea : 100 HP, según el meteorito te quita tanto. cuando vida 75% amarillo mitad naranja cuando -de la mitad rojo
- PROYECTO API Clima
- Base de datos de score.
- Colisiones
"""
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
            if self.sumayup <= 50: # este valor lo saqué fijandome en que valor se quedaba presionando 2 sec aprox.
                self.speed_y = -2
                self.contadory = 1 # contador
                self.image = pygame.image.load("recursos/nave/subir.png").convert_alpha() 
            if self.sumayup > 50: 
                self.speed_y = -5
                self.image = pygame.image.load("recursos/nave/subir fuerte.png").convert_alpha() #por fin doy uso a mi tan preciada imagen.

        # dar movimiento DOWN   
        if presiona[pygame.K_s]:
            self.sumayup = self.sumayup*0
            if self.sumaydw <= 50:  
                self.speed_y = 2
                self.contadory = 1
                self.image = pygame.image.load("recursos/nave/bajar.png").convert_alpha()
            if self.sumaydw > 50:
                self.speed_y = 5
                self.image = pygame.image.load("recursos/nave/bajar fuerte.png").convert_alpha()

        self.sumayup += self.contadory
        #print(self.sumayup)
        self.sumaydw += self.contadory
        #print(self.sumaydw)

        self.rect.y += self.speed_y

        if self.rect.bottom > alto:
            self.rect.bottom = alto
        if self.rect.bottom < 50:
            self.rect.bottom = 50


# METEORITOS

class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/METEORITOS/CCC.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(negro)
        self.rect.centerx = 750 # X
        self.rect.centery= random.randrange(25, 575) # Y
        # A DETERMINAR LA VELOCIDAD
        self.speedy = 0 #random.randrange(-5, 5)
        self.speedx = random.randrange(5, 10)
        # meto aquí esto ya que si lo pongo en linea 56 me casca [es un parche, no me bajes nota Pigmonchu por fa plis]
        self.image = random.choice(meteoritos_imagenes)
        #metiendo rotachione a los meteoritos    
    def update(self):
        self.rect.centerx -= self.speedx
        self.rect.centery += self.speedy
        if self.rect.centery < -50 or self.rect.centerx < -50 or self.rect.centery > ancho + 50 : 
            self.rect.centerx = 750 # X
            self.rect.centery= random.randrange(25, 575)
            self.speedx = random.randrange(5, 10)


# ZONA DE DECLARAR IMAGENES

meteoritos_imagenes=[]
lista_de_meteoritos=["recursos/METEORITOS/CCC.png","recursos/METEORITOS/I.png","recursos/METEORITOS/IV.png","recursos/METEORITOS/L.png","recursos/METEORITOS/MIX.png","recursos/METEORITOS/XDV.png"]
for img in lista_de_meteoritos:
    meteoritos_imagenes.append(pygame.image.load(img).convert_alpha())



# LA IMAGEN DE FONDO QUE CAMBIARÉ SEGÚN CLIMA
fondo = pygame.image.load("recursos/fondo.png").convert()
""" 
fondo_lluvia = pygame.image.load("recursos/fondo.png").convert()
fondo_nubes = pygame.image.load("recursos/fondo.png").convert()
""" 
# -----------------------------------------------

GAME_OVER = True
STAY_ALIVE = True
while STAY_ALIVE:
    
    if GAME_OVER:
        
        GAME_OVER = False
        all_sprites = pygame.sprite.Group()
        lista_de_meteoritos = pygame.sprite.Group()
        nave = Nave()
        all_sprites.add(nave)
        for n in range(5):
            meteoritos=Meteoritos()
            all_sprites.add(meteoritos)
            lista_de_meteoritos.add(meteoritos)
        
        score = 0

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False
        
        elif event.type == pygame.KEYDOWN:
            """
            if event.key == pygame.K_SPACE:
                player.shoot()
            """
      
    all_sprites.update()

    """"
    #                                                              True ya que los objetos que choquen desaparecen
    golpes = pygame.sprite.spritecollide(nave, lista_de_meteoritos, True)
    
    """ 
    """ 
    if tiempo == 'Clouds':
        ventana.blit(fondo, [0, 0])
        ventana.blit(fondo_nubes, [0, 0])
    elif tiempo == 'Rain':
        ventana.blit(fondo, [0, 0])
        ventana.blit(fondo_lluvia, [0, 0])
    else:
    """ 
    ventana.blit(fondo, [0, 0])

    all_sprites.draw(ventana)
  
    #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

    pygame.display.flip()
pygame.quit()