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

    house = pygame.image.load('images/barn_V2.png').convert_alpha()

    houseX = 50
    houseY = WINDOW_HEIGHT - house.get_width()

    house_mask = pygame.mask.from_surface(house)
    mask_h = house_mask.to_surface()

    ## test cropping
    tileX = 125
    tileY = 75
    cropX = 0
    cropY = 0
    cropWidth = 5
    cropHeight = 5



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


        # WINDOW.blit(mask_h, (tileX, tileY), (cropX, cropY, cropWidth, cropHeight))
        
        # WINDOW.blit(house, (houseX, houseY))

        for h in range(4):
          WINDOW.blit(house, (houseX + h*200, houseY))

        # WINDOW.blit(mask_h, (0,0))

    

        pygame.display.update()
        fpsClock.tick(FPS)
 
main()