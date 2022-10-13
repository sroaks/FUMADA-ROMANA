import pygame, random
from tiempop import *

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

print(tiempo)
print(v_viento)

class Clima(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/efectos_clima/sol_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery= 300

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
        self.spin = random.randrange(0,359)

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
fondo = pygame.image.load("recursos/fondo.png").convert_alpha()

# -----------------------------------------------


    

GAME_OVER = True
STAY_ALIVE = True
while STAY_ALIVE:

    
    if GAME_OVER:
        
        GAME_OVER = False
        all_sprites = pygame.sprite.Group()
        lista_de_meteoritos = pygame.sprite.Group()

        for n in range(5):
            meteoritos=Meteoritos()
            clima=Clima()
            all_sprites.add(meteoritos)
            lista_de_meteoritos.add(meteoritos)
            all_sprites.add(clima)
        
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
    ventana.fill(blanco)

    all_sprites.draw(ventana)



    pygame.display.flip()
pygame.quit()