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

class brickModel(object):
    
    def __init__(self, x, y, imgX, imgY): 
        '''
        add params here that are like alientype and aniframe - blockX & blockY 
        indicate where at in barn image for easy calling later (since will have diff x positions for each new barn in the set.)
        '''
        self.x = x
        self.y = y
        self.imgX = imgX # coords of barn sprite for each brick doesn't change for each barn
        self.imgY = imgY

class barnBuilder(object):
    
    def __init__(self):
        self.bricks = []
        # self.barns = []
        # for row in range(10):
        #     for col in range(10):
        #         brick = brickModel(col * 10, row * 10, )
        #         self.bricks.append(brick)
        for b in range(50, 800, 200): 
            for row in range(10):
                for col in range(10):
                    brick = brickModel((col * 10) + b, (row*10) + (WINDOW_HEIGHT - 100), col * 10, row * 10)
                    self.bricks.append(brick)
            # self.barns.append(self.bricks)
            # bricks = []

        for b in self.bricks:
            print('x: ', b.x, 'y: ', b.y)

class barnView:
    
    def __init__(self, bricks, imgpath):
        self.image = pygame.image.load(imgpath)
        self.bricks = bricks

    def render(self, surface):
        for b in self.bricks.bricks:
            surface.blit(
                self.image,
                (b.x, b.y),  # these should be in the brick info otherwise bullet can't collide with it properly
                (b.imgX, b.imgY, 10, 10),
            )
 
# The main function that controls the game
def main ():
    looping = True

    image = pygame.image.load('images/barn_V2.png').convert_alpha()
    
    imgpath = 'images/barn_V2.png'

    barn = barnBuilder()
    barn_view = barnView(barn, imgpath)

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

        

        # for brick in barn.bricks:
        #     WINDOW.blit(image, (brick.x, (WINDOW_HEIGHT - 100) + brick.y), (brick.x, brick.y, 10, 10) )
        barn_view.render(WINDOW)

        
        pygame.display.update()
        fpsClock.tick(FPS)
 
main()