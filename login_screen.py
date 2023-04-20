import pygame, sys, random, os
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (0, 0, 0)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hack Me')
        
text_str1 = '''
0x0990 /+/`#!#.\<@)
0x0991 >*~}}(#>`"]<
0x0992 |?`|+/">,^{{
0x0993 QUEEN\)"\/:}
0x0994 [&\@@:[,<\&@
0x0995 &*:|.]`^\@!(
0x0996 |*\@`&*#);+*
0x0997 `^*^=">;%+]*
0x0998 |$"-|)/&.=~<
0x0999 [\{.&\;*-@,@
0x099a ~?+~&%._<%['
0x099b ;&]:}`|}:~#`
0x099c =='`*$>[\.~>
0x099d -"@$!<#`*#|&
0x099e ;-`^`"?/^|~_
0x099f >[*.>;][`#~/
'''

text_str2 = '''
0x09a0 @{?APPLE;@{?
0x09a1 ,^"+%>WOMAN>
0x09a2 ,$(=}/,?.,-?
0x09a3 \?<@)IDIOT@)
0x09a4 `[};'LAUGH;'
0x09a5 |);+!\|,:$}#
0x09a6 @%%%)~%-{(\+
0x09a7 :*`_(?(;$;/#
0x09a8 >,(~,_.+:`<}
0x09a9 ({<!%/~<&.?-
0x09aa ^.{;>;.$-_@?
0x09ab :%>>#)~.[_}_
0x09ac $]\*|"../?~=
0x09ad $\#:"}%=":*/
0x09ae /|_@>#?`+#=)
0x09af "#//]'?>=/";
'''

# text_str = '''0x0990 /+/`#!#.\<@) 0x0991 >*~}}(#>`"]< 0x0992 |?`|+/">,^{{ 0x0993 QUEEN\)"\/:}'''
# text_str = '0x0990 /+/`#!#.\<@)'
font = pygame.font.Font(os.path.join('images', 'Share-TechMono.ttf'), 20)
# text_str = '0x0990 /+/`#!#.\<@)'
text_col1 = font.render(text_str1, True, (0, 238, 0), None)
text_col2 = font.render(text_str2, True, (0, 238, 0), None)
text_rect_1 = text_col1.get_rect()
text_rect_2 = text_col2.get_rect()
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
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    
    # WINDOW.blit(text, (0, 0))
    WINDOW.blit(text_col1, (10,0)) # print on rectangle
    WINDOW.blit(text_col2, (240, 0)) # print on rectangle
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()