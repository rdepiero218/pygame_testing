# Highlight-able menu in Pygame
#
# To run, use:
#     python pygame-menu-mouseover.py
#
# You should see a window with three grey menu options on it.  Place the mouse
# cursor over a menu option and it will become white.

import pygame, sys

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        pygame.draw.rect(screen, self.get_background(), (0, self.pos[1], 480, 25))
        screen.blit(self.rend, self.rect)
        # self.text_rect = pygame.Surface(self.rend.get_rect())
        # self.text_rect.fill(self.get_background())
        # self.text_rect.blit(self.rend, self.rect)
        

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        # print(self.pos)
        # print(self.rend.get_rect().size)
        # self.text_rect = pygame.Surface(self.rend.get_rect())
        # print('rect: ', self.text_rect.get_rect())
        # self.text_rect.fill(self.get_background())

    def get_color(self):
        if self.hovered:
            return (0, 0, 0)
        else:
            return (0, 238, 0)
    
    def get_background(self):
        if self.hovered:
            return (0, 238, 0)
        else:
            return (0, 0, 0)
   
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
screen = pygame.display.set_mode((480, 320))
menu_font = pygame.font.Font('images/Share-TechMono.ttf', 20)
x_offset = 10
options = [Option("[Personal Logs]", (x_offset, 105)), 
           Option("[Turret Control]", (x_offset, 155)),
           Option("[Safe Control]", (x_offset, 205))]
while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    pygame.display.update()