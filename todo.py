import pygame, random, sys

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

font = pygame.font.SysFont('Arial', 15)

def draw_text(text,font,color,ventana,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    ventana.blit(textobj,textrect)



"""
"""
"""
TO DO LIST:
- Rotar los meteoritos (hecho, pero hay que ajustarlo)
- PROYECTO BARRA DE VIDA, idea : 100 HP, según el meteorito te quita tanto. cuando vida 75% amarillo mitad naranja cuando -de la mitad rojo
-
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
        #print(self.sumayup)
        self.sumaydw += self.contadory
        #print(self.sumaydw)

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


# ZONA DE DECLARAR IMAGENES

meteoritos_imagenes=[]
lista_de_meteoritos=["recursos/METEORITOS/CCC.png","recursos/METEORITOS/I.png","recursos/METEORITOS/IV.png","recursos/METEORITOS/L.png","recursos/METEORITOS/MIX.png","recursos/METEORITOS/XDV.png"]
for img in lista_de_meteoritos:
    meteoritos_imagenes.append(pygame.image.load(img).convert_alpha())

fondo = pygame.image.load("recursos/fondo.png").convert()


# ---------- metiendo clima -----------------------

POSI_C = (700,15)
POSI_BRUJ = (623, 37)
POSI_GRADOS = (600,15)
# import de la API : clima
clima = tiempo


img_clima = pygame.image.load("recursos/efectos_clima/nube01.png").convert_alpha()
img_brujula_v = pygame.image.load("recursos/efectos_clima/brújula.png").convert_alpha()
img_grados_v = pygame.image.load("recursos/efectos_clima/grados_brjula.png").convert_alpha()

imgl=[]
if clima == 'Clouds':
    imgl_row= ['recursos/efectos_clima/nube01.png','recursos/efectos_clima/nube02.png','recursos/efectos_clima/nube03.png']
if clima == 'Clear':
    imgl_row= ['recursos/efectos_clima/sol_1.png','recursos/efectos_clima/sol_2.png','recursos/efectos_clima/sol_3.png']
if clima == 'Rain':
    imgl_row= ['recursos/efectos_clima/nube01.png','recursos/efectos_clima/nube02.png','recursos/efectos_clima/nube03.png']

for img in imgl_row:
    imgl.append(pygame.image.load(img).convert_alpha())


    
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



GAME_OVER = True
STAY_ALIVE = True

aux = 1 # variable para tiempo numero entero
while STAY_ALIVE:
    t = pygame.time.get_ticks()//1000
    G = 0
    if aux == t:
        aux += 1
        x = list(divmod(t,3))
        if x[1] == 1:
            img_clima= imgl[0]
        if x[1] == 2:
            img_clima= imgl[1]
        if x[1] == 0:
            img_clima= imgl[2]
    
    # ROTACIÓN BRUJULA SEGUN GRADOS API

    
    if GAME_OVER:
        
        GAME_OVER = False
        
        score = 0

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STAY_ALIVE = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nave.shoot()
        
      
    all_sprites.update()
    # Colisiones disparos
    hits = pygame.sprite.groupcollide(lista_de_meteoritos, bullets, True, True)
    for hit in hits:
        meteor = Meteoritos()
        all_sprites.add(meteor)
        lista_de_meteoritos.add(meteor)
		
	# Colisiones jugador - meteoro
    hits = pygame.sprite.spritecollide(nave, lista_de_meteoritos, False)
    if hits:
        running = False


    ventana.blit(fondo, [0, 0])

    all_sprites.draw(ventana)

    ventana.blit(img_clima,POSI_C)
    ventana.blit(img_grados_v, POSI_GRADOS)
    ventana.blit(pygame.transform.rotate(img_brujula_v,grados_viento),POSI_BRUJ)

    draw_text(str(t),font,(0,0,0),ventana, 20, 20)
    draw_text('Vel-viento m/s:',font,(rojo),ventana,450,10)
    draw_text(str(velocidad_viento),font,(rojo),ventana,545,10)
  
    #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

    pygame.display.flip()
pygame.quit()