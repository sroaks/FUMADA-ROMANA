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

class Enemigo():
    def show(self):
        ventana.blit(picture1,[200,300])

enemigo = Enemigo()
q = 0
aux = 1
contadorimg = 0
while STAY_ALIVE:
    ventana.blit(dungeon, [0, 0])
    t = pygame.time.get_ticks()//1000
    if aux == t:
        aux += 1
        q = t
        x = list(divmod(q,2))
        print(x[1])
        if x[1] == 1:
            picture = picture1
        if x[1] == 0:
            picture = picture2
            
    enemigo.show(picture)

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
    
 
    ventana.blit(img,loc)
    ventana.blit(interior, [0, 0])
    draw_text(str(q),font_2,(blanco), ventana, 40, 220)
    pygame.display.flip()
pygame.quit()