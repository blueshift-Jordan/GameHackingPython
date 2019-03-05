#importing pygame
import pygame, sys
from pygame.locals import *

#initialising pygame
pygame.init()

#set up game window
DISPLAYSURF = pygame.display.set_mode((400, 300))

#caption game window
pygame.display.set_caption('Hello Pygame World!')

# main game loop
while True:


    #IDLE friendly quitting
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

