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
screenwidth = 500

isjump = True
jumpcount = 10
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
        
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < screenwidth - width - vel:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel
            
    if keys[pygame.K_DOWN] and y < screenwidth - height - vel:
        y += vel

    


    win.fill((0,0,0))
        
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))#5 drawing shapes 1st the surface , 2nd the color (RGB), X Y coordinates, height and width
    pygame.display.update();
pygame.quit