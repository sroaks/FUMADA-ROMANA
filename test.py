import pygame, random

pygame.init()
clock = pygame.time.Clock()


    
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

picture1=pygame.image.load("recursos/NAVE_2/ENEMI_01_01.png").convert_alpha()
picture2=pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
picture = [picture1 , picture2]
contadorE = 0

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
        self.image.set_colorkey(naranja)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(150,550)
        self.rect.centery = 300
        self.posi = [self.rect.centerx,self.rect.centery]
        self.vx = 0
        self.vy = 0
    def update(self):
        t = pygame.time.get_ticks()//1000
        self.priedra_angular_del_averno_infernal = list(divmod(t,2))
        self.contador_infernal = 0
        if self.priedra_angular_del_averno_infernal[1] == 0 and self.contador_infernal == 0:
            self.image = pygame.image.load("recursos/NAVE_2/ENEMI_01_01.png").convert_alpha()

            self.vx += 0.5
            self.vy += 0.5

            self.contador_infernal += 1
        if self.priedra_angular_del_averno_infernal[1] == 1 and self.contador_infernal == 1:
            self.image = pygame.image.load("recursos/NAVE_2/ENEMI_01_02.png").convert_alpha()
            """
            self.vx += 0.5
            self.vy += 0.5
            """
            self.contador_infernal -= 1

        print(self.contador_infernal)
        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        self.posi = [self.rect.centerx,self.rect.centery]
        """
        if self.x < 0 or self.y > ancho + 10 or self.y > 650:
                self.rect.centerx = random.randrange(200,400)
                self.y = 300
                self.rect.centerx += 0.5
                self.rect.centery += 0.5
        """
enemigo1_sprites = pygame.sprite.Group()

for n in range(2):
    enemigo = Enemigo()
    enemigo1_sprites.add(enemigo)

t = pygame.time.get_ticks()//1000
q = 0

fps = 60
segundos = 0
while STAY_ALIVE:
    clock.tick(fps)
    if t > 0:
        q += 1
        segundos = round(q * 1/fps ,0)
        
    ventana.blit(dungeon, [0, 0])
    picturet = pygame.transform.scale(picture1, (20,24))
        
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
    
    if segundos >= 2:
        enemigo1_sprites.draw(ventana)
        enemigo1_sprites.update()
 
    ventana.blit(img,loc)
    ventana.blit(interior, [0, 0])
    draw_text(str(segundos),font_2,(blanco), ventana, 40, 220)
    pygame.display.flip()
pygame.quit()