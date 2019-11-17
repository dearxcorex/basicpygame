import pygame
import random
 
WIDTH = 800
HEIGHT = 600
FPS = 30 
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED  = (255,0,0)
GREEN = (0,255,0)
BLUE  =  (0,0,255)

class player(pygame.sprite.Sprite):
    #sprite is a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  =  pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 , HEIGHT / 2 )


    def update(self):
        self.rect.x += 5 

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('my gamex')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = player()
all_sprites.add(player)
#main loop 
running = True 

while running:
    # keep loop running at
    clock.tick(FPS)

    #process input(events)
    for event in pygame.event.get():
        #print(event)
        #check for closeing window 
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    #Draw / render 
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everthing flip the display 
    pygame.display.flip()

pygame.quit()