import pygame, random

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SPQR")
clock = pygame.time.Clock()
"""
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
        self.speed_x = 0
        self.vida = 100
    def update(self):
        presiona = pygame.key.get_pressed()
        mantiene = 0
        self.speed_y = 0
        if presiona != True or mantiene != True:
             self.image = pygame.image.load("recursos/nave/NORMAL.png").convert_alpha()            
        if presiona[pygame.K_w]:
            self.speed_y = -10
            self.image = pygame.image.load("recursos/nave/subir.png").convert_alpha()
        """
        Quiero que cuando se mantenga pulsado acelere y cambia img
        if mantiene[pygame.K_w]:
            self.speed_y = -5
            self.image = pygame.image.load("recursos/nave/subir fuerte.png").convert_alpha()
            
        """
        if presiona[pygame.K_s]:
            self.speed_y = 10
            self.image = pygame.image.load("recursos/nave/bajar.png").convert_alpha()
        self.rect.y += self.speed_y
        if self.rect.bottom > alto:
            self.rect.bottom = alto
        if self.rect.bottom < 50:
            self.rect.bottom = 50

# METEORITOS

class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(negro)
        self.image = random.choice(meteoritos_imagenes)
        self.rect.centerx = 750 # X
        self.rect.centery= random.randrange(25, 575) # Y
        # A DETERMINAR LA VELOCIDAD
        self.speedy = 0 #random.randrange(-5, 5)
        self.speedx = random.randrange(5, 10)
    
    def update(self):
        self.rect.centerx -= self.speedx
        self.rect.centery += self.speedy
        #en el caso de que se salga que aparezca de nuevo
        if self.rect.centery < -50 or self.rect.centerx < -50 or self.rect.centery > ancho + 50 : 
            self.rect.centerx = 750 # X
            self.rect.centery= random.randrange(25, 575)
            self.speedx = random.randrange(5, 10)

# ZONA DE DECLARAR IMAGENES

meteoritos_imagenes=[]
lista_de_meteoritos=["recursos/METEORITOS/CCC.png","recursos/METEORITOS/I.png","recursos/METEORITOS/IV.png","recursos/METEORITOS/L.png","recursos/METEORITOS/MIX.png","recursos/METEORITOS/XDV.png"]
for img in lista_de_meteoritos:
    meteoritos_imagenes.append(pygame.image.load(img).convert_alpha())


all_sprites = pygame.sprite.Group() # GRUPO PARA LA NAVE
lista_de_meteoritos = pygame.sprite.Group()
#lista_de_meteoritos = pygame.sprite.Group() # '' / METEORITOS

nave = Nave() # crea la nave para meterla en all_sprites
all_sprites.add(nave)

#meteorito = Meteorito() # crea el meteorito para meterlo en all_sprites
#all_sprites.add(meteorito)

for n in range(5): # iteramos sobre un rango de 5 para crear varios meteoritos
    meteoritos=Meteoritos()
    all_sprites.add(meteoritos)
    lista_de_meteoritos.add(meteoritos)

# -----------------------------------------------

GAME_OVER = True
STAY_ALIVE = True
while STAY_ALIVE:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False
    
    #ventana.fill((blanco))
      
    all_sprites.update() # meto all_sprites

    fondo = pygame.image.load("recursos/fondo.png").convert()
    ventana.blit(fondo, [0, 0]) #dibujar muchas imágenes en otra

    all_sprites.draw(ventana) # dibujo all_sprites
  
    #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

    pygame.display.flip()
pygame.quit()