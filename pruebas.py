import pygame, random

ancho = 800
alto = 600
negro = (0, 0, 0)
blanco = (255, 255, 255)

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("SPQR")
clock = pygame.time.Clock()

# MI NAVE




# METEORITOS

class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/METEORITOS/CCC.png").convert_alpha()
        self.rect = self.image.get_rect()
    def rotar(self):
        self.rotate = pygame.transform.rotate(self.image, 180)


all_sprites = pygame.sprite.Group() # GRUPO PARA LA NAVE
lista_de_meteoritos = pygame.sprite.Group()


for n in range(5):
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

    ventana.fill((blanco))


    pygame.display.flip()
pygame.quit()

