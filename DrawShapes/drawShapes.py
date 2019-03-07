import pygame

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

    # Rectangle
    pygame.draw.rect(screen, (0,255,0), (100, 100, 200, 100))

    # Circle
    pygame.draw.circle(screen, (255,0,0), (300, 250), 100)

    points = [(400, 30), (500, 300), (300, 300), (400, 30)]
    pygame.draw.polygon(screen, BLUE, points)

    points = [(50, 200), (200, 50), (280, 300), (200, 350), (100, 300)]
    pygame.draw.lines(screen, WHITE, True, points)

    # AFTER DRAWING EVERYTHING
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

