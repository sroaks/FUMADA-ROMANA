import pygame, random

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

"""

lista_de_meteoritos=["recursos/METEORITOS/CCC.png","recursos/METEORITOS/I.png","recursos/METEORITOS/IV.png","recursos/METEORITOS/L.png","recursos/METEORITOS/MIX.png","recursos/METEORITOS/XDV.png"]
meteoritos_imagenes=[]
for img in lista_de_meteoritos:
    meteoritos_imagenes.append(pygame.image.load(img).convert_alpha())
"""

class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/METEORITOS/I.png").convert_alpha()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect() # Saco la recta de la imagen para definir su posicion
        self.rect.centerx = 750 # X
        self.rect.centery= random.randrange(25, 575) # Y
        # A DETERMINAR LA VELOCIDAD
        self.speedy = 0 #random.randrange(-5, 5)
        self.speedx = random.randrange(5, 10)
    
    def update(self):
            self.rect.centerx -= self.speedx
            self.rect.centery += self.speedy
            #en el caso de que se salga que aparezca de nuevo
            if self.rect.centery < -50 or self.rect.centerx < -50 or self.rect.y > ancho + 50 : 
                self.rect.centerx = 750 # X
                self.rect.centery= random.randrange(25, 575)
                self.speedx = random.randrange(5, 10)