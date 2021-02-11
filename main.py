import pygame # library
pygame.init()

class Brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    def draw(self):
        if self.alive == True:
            pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 50, 20))
    def collide(self, x, y):
        if self.alive == True:
            if x+20>self.xpos and x<self.xpos+50 and y+20> self.ypos and y < self.ypos +20:
                self.alive = False
                return True

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("breakout")
clock = pygame.time.Clock()

doExit = False
px = 300
py = 450

bx = 200
by = 200

bVx = 5
bVy = 5

# create a bunch of bricks!
b1 = Brick(0, 0)
b2 = Brick(50, 0)
b3 = Brick(100, 0)
b4 = Brick(150, 0)
b5 = Brick(200, 0)
b6 = Brick(250, 0)
b7 = Brick(0, 0)
b8 = Brick(0, 0)
b9 = Brick(0, 0)
b10 = Brick(0, 0)
while not doExit: #__________________game loop_____________

    #I/O section.....................................
    
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        px -= 5
    if keys[pygame.K_d]:
        px += 5
    
    # physics section...........................
    
    #move the ball 
    bx += bVx
    by += bVy
    
    # bounce of ceiling floor and walls
    if bx < 0 or bx > 680:
        bVx *= -1
    if by < 0 or by > 480:
        bVy *= -1
    
    #paddle bounce collision
    if by + 20 > py and bx + 20 > px and bx < px + 100:
        bVy *= -1
    
    if b1.collide(bx, by):
        bVy *= -1
    
    
    #render section.......................................
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255, 255, 255), (px, py, 100, 20))
    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 20))
    
    
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()

    
    pygame.display.flip()
            
            
#end game loop_______________________
pygame.quit()
