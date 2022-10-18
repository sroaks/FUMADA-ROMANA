import pygame, random, sys

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
        nave_y_bala_sprites.add(bullet)
        bullets.add(bullet)

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


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
lista_de_meteoritos = pygame.sprite.Group()

nave = Nave()

all_sprites.add(nave)
