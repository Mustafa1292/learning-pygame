import pygame


pygame.init()


win = pygame.display.set_mode((500,480))


pygame.display.set_caption("My game")

walkRight = [pygame.image.load('game/R1.png'), pygame.image.load('game/R2.png'), pygame.image.load('game/R3.png'), pygame.image.load('game/R4.png'), pygame.image.load('game/R5.png'), pygame.image.load('game/R6.png'), pygame.image.load('game/R7.png'), pygame.image.load('game/R8.png'), pygame.image.load('game/R9.png')]
walkLeft = [pygame.image.load('game/L1.png'), pygame.image.load('game/L2.png'), pygame.image.load('game/L3.png'), pygame.image.load('game/L4.png'), pygame.image.load('game/L5.png'), pygame.image.load('game/L6.png'), pygame.image.load('game/L7.png'), pygame.image.load('game/L8.png'), pygame.image.load('game/L9.png')]
bg = pygame.image.load('game/bg.jpg')
char = pygame.image.load('game/standing.png')

clock = pygame.time.Clock()
x = 50 
y = 400

width = 64
height = 64
vel = 5 
screenwidth = 500
isjump = False
jumpcount = 10
left = False
right = False
walkcout = 0

def redrawGameWindow():
    global walkcout
    win.blit(bg, (0,0))        
    if walkcout + 1 >= 27:
        walkcout = 0
    if left:
        win.blit(walkLeft[walkcout//3], (x,y))
        walkcout += 1
    elif right:
        win.blit(walkRight[walkcout//3], (x,y))
        walkcout += 1
    else: 
        win.blit(char, (x,y))
    pygame.display.update();

running = True
while running:
    clock.tick(27)
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

        
    keys = pygame.key.get_pressed() 
        
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < screenwidth - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkcout = 0
    if not (isjump):
        #if keys[pygame.K_UP] and y > vel:
        #    y -= vel
                
        #if keys[pygame.K_DOWN] and y < screenwidth - height - vel:
        #    y += vel

        if keys[pygame.K_SPACE]:
            isjump = True
            right = False
            left = False
    else:
        if jumpcount >= -10:
            y -= (jumpcount * abs(jumpcount)) * 0.5
            jumpcount -= 1
        else: 
            jumpcount = 10
            isjump = False
        

    redrawGameWindow()

    
pygame.quit