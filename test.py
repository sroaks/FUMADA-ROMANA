import pygame, random, sys

from tiempop import *

from nave import *

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
fotn_2 = pygame.font.SysFont('Arial', 25)

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
- Base de datos de score
- Editar los textos cada uno con una fuente color tamaño etc...
- MENU
- METER TIMING (QUE EMPIECE DETERMINADOS SEGUNDOS, PARE, SUME METEORITOS, DIFERENTES ENEMIGOS...)
- diferenciar los sprites para poder darles el timing... meteoritos por un lado otros enemigos por otro etc, asi controlas más
- DEFINIR WIN
- LVL 2
- BASE DE DATOS en este enlace: https://www.youtube.com/watch?v=4FDVzF0Z9Yo&list=WL&index=5&ab_channel=UskoKruM2010

"""
# MI NAVE




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

fondo = pygame.image.load("recursos/fondo.png").convert()

explosion_anim = []
for i in range(7):
	file = "recursos/explosion/EXP0{}.png".format(i)
	img = pygame.image.load(file).convert_alpha()
	img.set_colorkey(negro)
	img_scale = pygame.transform.scale(img, (70, 70))
	explosion_anim.append(img_scale)


# ---------- metiendo clima -----------------------

POSI_C = (700,15)
POSI_BRUJ = (623, 37)
POSI_GRADOS = (600,15)
# import de la API : clima
clima = tiempo


img_clima = pygame.image.load("recursos/efectos_clima/nube01.png").convert_alpha()
img_brujula_v = pygame.image.load("recursos/efectos_clima/brújula.png").convert_alpha()
img_grados_v = pygame.image.load("recursos/efectos_clima/grados_brjula.png").convert_alpha()

imgl = []
for w in range(3):
	file = 'rsecursos/efectos_clima/nube0{}.png'.format(w)
	img = pygame.image.load(file).convert_alpha()
	img.set_colorkey(negro)
	#img_scale = pygame.transform.scale(img, (70, 70))
	imgl.append(img)

#-- SCORE EN NUMERO ROMANO 

nr=[
    (1000,'M'), (500, 'D'),
    (100,'C'), (50,'L'),
    (10,'X'), (5,'V'),(1,'I')
    ]

    
# -----------------------------------------------------


lista_de_meteoritos = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

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
        vida = 100


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
        score += 1
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        meteor = Meteoritos()
        all_sprites.add(meteor)
        lista_de_meteoritos.add(meteor)
		
	# Colisiones jugador - meteoro
    hits = pygame.sprite.spritecollide(nave, lista_de_meteoritos, True)
    if hits:
        STAY_ALIVE = False


    # SCORE N_ROMAN

    N=score
    N="{:0>4d}".format(N)
    Nlista=list(N)

    millares=int(Nlista[0])
    centenas=int(Nlista[1])
    decenas=int(Nlista[2])
    unidades=int(Nlista[3])
    nu=""
    nd=""
    nc=""
    nm=""
    #unidades
    if unidades<9 and unidades>=5:
        nu=(nr[5][1]+(unidades-5)*nr[6][1])
    elif unidades<4:
        nu=(unidades*nr[6][1])
    elif unidades==4:
        nu='IV'
    elif unidades==9:
        nu='IX'
    #decenas
    if decenas<9 and decenas>=5:
        nd=(nr[3][1]+((decenas-5)*nr[4][1]))
    elif decenas>=1 and decenas<4:
        nd=(nr[4][1])*decenas
    elif decenas==4:
        nd='XL'
    elif decenas==9:
        nd='XC'   
    #centenas
    if centenas<9 and centenas>=5:
        nc=(nr[1][1]+(centenas-5)*nr[2][1])
    elif centenas>=1 and centenas<4:
        nc=(nr[2][1])*centenas
    elif centenas==4:
        nc='CD'
    elif centenas==9:
        nc='CM'
    #millares
    if millares>=1 and millares<4:
        nm=(nr[0][1])*millares
    else:
        N=(nm+nc+nd+nu)


    ventana.blit(fondo, [0, 0])

    all_sprites.draw(ventana)

    ventana.blit(img_clima,POSI_C)
    ventana.blit(img_grados_v, POSI_GRADOS)
    ventana.blit(pygame.transform.rotate(img_brujula_v,grados_viento),POSI_BRUJ)

    draw_text(str(N), font, (negro), ventana, 400, 20)
    draw_text(str(t),font,(negro), ventana, 20, 20)
    draw_text('Vel-viento m/s:',font,(rojo),ventana,450,10)
    draw_text(str(velocidad_viento),font,(rojo),ventana,545,10)
  
    #pygame.draw.rect(ventana, (negro),(ancho/2,alto/2, 50, 50)) probando las capas.

    pygame.display.flip()
pygame.quit()