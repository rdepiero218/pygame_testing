import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (0, 0, 0)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 600
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
 
# The main function that controls the game
def main ():
    looping = True

    ## test cropping
    tileX = 0  ## x position you want it to be
    tileY = 0
    cropX = 0   # position to crop
    cropY = 150
    cropWidth = 150
    cropHeight = 150

    tileSprite = pygame.image.load('images/reaction_sprite.png').convert_alpha()

    # The main game loop
    while looping :
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later

        # Render elements of the game
        WINDOW.fill(BACKGROUND)

        WINDOW.blit(tileSprite, (tileX, tileY), (cropX, cropY, cropWidth, cropHeight))
        pygame.display.update()
        fpsClock.tick(FPS)
    
main()