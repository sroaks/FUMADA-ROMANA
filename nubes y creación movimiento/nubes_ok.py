import pygame



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

# ---------- metiendo clima -----------------------

POSI_C = (700,35)
# import de la API : clima
clima = 'Clear'
img_clima = pygame.image.load('img/nube01.png').convert_alpha()

imgl=[]

if clima == 'Clouds':
    imgl_row= ['img/nube01.png','img/nube02.png','img/nube03.png']
if clima == 'Clear':
    imgl_row= ['img/nube01.png','img/nube02.png','img/nube03.png']
if clima == 'Rain':
    imgl_row= ['img/nube01.png','img/nube02.png','img/nube03.png']

for img in imgl_row:
    imgl.append(pygame.image.load(img).convert_alpha())
    
# -----------------------------------------------------

"""
"""

background = pygame.image.load("img/blanco.png").convert()

game_over = True
running = True

aux = 1
while running:
    #screen.fill(WHITE)
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
                        
    """
    """
    if game_over:
        game_over = False
        """
        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        score = 0
        """
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #all_sprites.update()
    
    screen.blit(background, [0, 0])
    
    screen.blit(img_clima,POSI_C)
    
    #all_sprites.draw(screen)
    
    pygame.display.flip()
pygame.quit()
