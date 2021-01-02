import pygame

#1 initiallize
pygame.init()

#2the game window
win = pygame.display.set_mode((500,500))

#game caption
pygame.display.set_caption("My game")

#3 character attributes

#character position    
x = 50 
y = 50

#character make
width = 40
height = 50
vel = 5 #velocity

#4 main loop where pygame checks for mouse and keyboard events

running = True
while running:
    pygame.time.delay(100)
    #check for events (inputs) 
    for event in pygame.event.get():  #check if exit button is entered
        if event.type == pygame.QUIT:
            running = False

        #6 what if a key is held down
    keys = pygame.key.get_pressed() #coordinates change with the arrow keys
        
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel
            
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_SPACE]:
        win.fill((0,0,0))
        
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))#5 drawing shapes 1st the surface , 2nd the color (RGB), X Y coordinates, height and width
    pygame.display.update();
pygame.quit