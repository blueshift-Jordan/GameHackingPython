import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Load image
alienImg = pygame.image.load('images/alien.png')

# Bounce variables
xPos = 0
yPos = 0
xSpeed = 3
ySpeed = 3

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.
    xPos += xSpeed
    yPos += ySpeed

    if xPos + alienImg.get_width() > width or xPos < 0:
        xSpeed = xSpeed * -1

    if yPos + alienImg.get_height() > height or yPos < 0:
        ySpeed = ySpeed * -1

    # Draw.
    screen.blit(alienImg, (xPos, yPos))

    pygame.display.flip()
    fpsClock.tick(fps)