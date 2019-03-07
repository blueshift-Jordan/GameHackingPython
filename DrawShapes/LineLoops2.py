import pygame, math

WIDTH = 600
HEIGHT = 400
FPS = 30

#define Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# initialise pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Shapes")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input
    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            running = False
    # Draw
    screen.fill((0,0,0))

    for i in range(200):

        radians_x = i / 20
        radians_y = i / 6

        x = int(200 * math.sin(radians_x)) + 200
        y = int(200 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, RED, (x,y), (x+5,y), 5)

    # AFTER DRAWING EVERYTHING
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()