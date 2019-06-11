         ### TEMPLATE sketch will not execute without edit ###

#Import the two Modules needed for this sketch 
import pygame
import random
 
# Define some colors
BLACK = (?, ?, ?)
WHITE = (?, ?, ?)
BLUE = (?, ?, ?)
GREEN = (?, ?, ?) 
RED = (?, ?, ?)
YOUR_COLOUR(S) = (?, ?, ?)

#Set up our variables
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = ?
 

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.colour = ?????
 
 
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball() #Ball instence 
         
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ???? # >>> We need to return our Ball() object here!
 
 
def main():
    """
    This is our main program.
    """
    pygame.init() 
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
         
    # Change your display caption:   HERE
    pygame.display.set_caption("Bouncing Balls")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    #Create an empty list
    ball_list = []
 
    #Create another instance
    ball = make_ball()
        
    #Add the instance to the list
    ball_list.append(ball)

 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)
 
        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed # >>> Fill in the (?)
            if ball.y > ??????_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ????.? > SCREEN_WIDTH - ????_???? or ball.x < BALL_SIZE:
                ball.change_x *= -1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the balls 
        for ball in ball_list:
             #DRAW YOUR OBJECT HERE --> https://www.pygame.org/docs/ref/draw.html
             
             ??????.????.???????(screen, ???, [????.x, ????.y, ??, ??], 0)    
    
                  
             #Don't forget to use ball.x and ball.y for the rect
 
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()

# --- Credits ---- #

#This code has been adapated from the original for teaching purposes
#Details of the original Author and code can be found below:
"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
