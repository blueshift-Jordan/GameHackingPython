#importing pygame
from pygame.locals import *

#initialising pygame
pygame.init()

#set up game window
screen = pygame.display.set_mode((400, 300))

#caption game window
pygame.display.set_caption('Hello Pygame World!')

# main game loop
while True:
    #Remember the '__'INDENT
    
    
    
    
    
    
    
    #^^START_GAME_CODE_HERE^^   

    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    #IDLE friendly quitting
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

