import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")


bg = pygame.image.load('Assets/bg.jpg')

clock = pygame.time.Clock()

class enemy(object):
    walkRight = [pygame.image.load('Assets/R1E.png'),
                 pygame.image.load('Assets/R2E.png'),
                 pygame.image.load('Assets/R3E.png'),
                 pygame.image.load('Assets/R4E.png'),
                 pygame.image.load('Assets/R5E.png'),
                 pygame.image.load('Assets/R6E.png'),
                 pygame.image.load('Assets/R7E.png'),
                 pygame.image.load('Assets/R8E.png'),
                 pygame.image.load('Assets/R9E.png'),
                 pygame.image.load('Assets/R10E.png'),
                 pygame.image.load('Assets/R11E.png')]
    
    walkLeft = [pygame.image.load('Assets/L1E.png'),
                pygame.image.load('Assets/L2E.png'),
                pygame.image.load('Assets/L3E.png'),
                pygame.image.load('Assets/L4E.png'),
                pygame.image.load('Assets/L5E.png'),
                pygame.image.load('Assets/L6E.png'),
                pygame.image.load('Assets/L7E.png'),
                pygame.image.load('Assets/L8E.png'),
                pygame.image.load('Assets/L9E.png'),
                pygame.image.load('Assets/L10E.png'),
                pygame.image.load('Assets/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        


def redrawGameWindow():
    win.blit(bg, (0,0))
    goblin.draw(win)    
    pygame.display.update()

#mainloop
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


