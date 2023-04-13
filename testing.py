import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (0,0,0)

GREEN = (0, 238, 0)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
 
# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
    # Processing
    # This section will be built out later
    x = 10
    y = 30
    w = 50
    h = 70
    rect1 = pygame.Rect(x, y, w, h)
    # rect1 = pygame.Rect((10,30), (50, 70))
    rect2 = pygame.Rect(x+60, y, w, h)

    ellipse1 = pygame.Rect(x+150, y, w, h)
    ellipse1 = pygame.Rect(x+150, y, w+50, h)
    
    # Render elements of the game
    WINDOW.fill(BACKGROUND)

    pygame.draw.rect(WINDOW, GREEN, rect1)
    pygame.draw.rect(WINDOW, GREEN, rect2, 2)

    #does not have object declared like rect
    pygame.draw.circle(WINDOW, GREEN, (x+30, y+150), 30)

    pygame.draw.ellipse(WINDOW, GREEN, ellipse1)
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()