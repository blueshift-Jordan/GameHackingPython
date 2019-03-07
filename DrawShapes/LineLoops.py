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

    y_offset = 0

    while y_offset < HEIGHT:
        pygame.draw.line(screen,RED,(0,10+y_offset),(WIDTH/2, HEIGHT/2),3)
        pygame.draw.line(screen,GREEN,(WIDTH,10+y_offset),(WIDTH/2, HEIGHT/2),3)
        y_offset = y_offset + 10

    x_offset = 0

    while x_offset < WIDTH:
        pygame.draw.line(screen,BLUE,(10+x_offset,0),(WIDTH/2, HEIGHT/2),3)
        pygame.draw.line(screen,WHITE,(10+x_offset,HEIGHT),(WIDTH/2, HEIGHT/2),3)
        x_offset = x_offset + 10

    # AFTER DRAWING EVERYTHING
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
