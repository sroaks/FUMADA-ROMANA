import pygame

from meteor_ import *

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

background = pygame.image.load("img/blanco.png").convert()

game_over = True
running = True

aux = 1
while running:
    
    if game_over:
        game_over = False
        """"""
        all_sprites = pygame.sprite.Group()
        meteor = Meteor()
        all_sprites.add(meteor)
        
        
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    all_sprites.update()
    
    screen.blit(background, [0, 0])
    
    all_sprites.draw(screen)
    
    pygame.display.flip()
pygame.quit()