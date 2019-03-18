import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

WIDTH = 400
HEIGHT = 600
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Shmup")

done = False
clock = pygame.time.Clock()

# Game loop
while not done:

    clock.tick(FPS)

    # Process inputs/events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw
    screen.fill(BLACK)

    # Flip the display
    pygame.display.flip()

pygame.quit()