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

# Scaling
#alienImg = pygame.transform.scale(alienImg, (50, 50))

# Rotation
#alienImg = pygame.transform.rotate(alienImg, 90)

# Game loop.
while True:
  screen.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update.

  # Draw.
  # Display image
  screen.blit(alienImg, (0,0))

  pygame.display.flip()
  fpsClock.tick(fps)