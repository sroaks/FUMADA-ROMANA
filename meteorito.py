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
            #self.image = random.choice(lista)
            self.image = pygame.image.load("recursos/METEORITOS/CCC.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(ancho - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)
            self.speedx = random.randrange(-5, 5)

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > alto + 10 or self.rect.left < -25 or self.rect.right > ancho + 22 :
                self.rect.x = random.randrange(ancho - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)