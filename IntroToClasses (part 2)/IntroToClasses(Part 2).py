import pygame

#Setup
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")
bg = pygame.image.load('Assets/bg.jpg')
clock = pygame.time.Clock()


class enemy():
    walkRight = [pygame.image.load('Assets/R1E.png')]
    walkLeft = [pygame.image.load('Assets/L1E.png')]

#Define enemy attributes 
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 3

#This function moves and draws my image
    def draw(self, win):
        self.move()
        if self.vel > 0:
            win.blit(self.walkRight[0], (self.x,self.y))
        else:
            win.blit(self.walkLeft[0], (self.x,self.y))
        
  #This function moves my image         
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel



#                      --- Draw a Frame ---

def redrawGameWindow():
    win.blit(bg, (0,0))
    goblin.draw(win)    
    pygame.display.update()

#                      --- Main Game Loop ---

#My Enemy   (startX, y, width, height, endX)
goblin = enemy(20, 310, 64, 64, 450)

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Draw
    redrawGameWindow()
    
    

pygame.quit()


