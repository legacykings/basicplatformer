import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
from winsound import Beep

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
a=4
d=5 
w=6
s=7



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
xpos2 = 400 #xpos of player
ypos2 = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
vx2 = 0 #x velocity of player
vy2 = 0 
keys = [False, False, False, False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
isOnGround2 = False


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
                Beep(500, 100)
            elif event.key == pygame.K_a:
                keys[a]=True
            elif event.key == pygame.K_d:
                keys[d]=True
            elif event.key == pygame.K_w:
                keys[w]=True
                Beep(500, 100)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_a:
                keys[a]=False
            elif event.key == pygame.K_d:
                keys[d]=False
            elif event.key == pygame.K_w:
                keys[w]=False
                
    
            
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=+3
        direction = RIGHT
    elif keys[a]==True:
        vx2=-3
       
    elif keys[d]==True:
        vx2=+3
       

    #turn off velocity
    else:
        vx = 0
        vx2 = 0
        
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    elif keys[w] == True and isOnGround2 == True: #only jump when on the ground
        vy2 = -8
        isOnGround2 = False
        direction = UP
    
    

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >550 and ypos+40 <670:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >350 and ypos+40 <570:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False    
        
        
    if xpos2>100 and xpos2<200 and ypos2+40 >750 and ypos2+40 <770:
        ypos2 = 750-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>200 and xpos2<300 and ypos2+40 >650 and ypos2+40 <670:
        ypos2 = 650-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>300 and xpos2<400 and ypos2+40 >750 and ypos2+40 <770:
        ypos2 = 750-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>400 and xpos2<500 and ypos2+40 >550 and ypos2+40 <670:
        ypos2 = 550-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>600 and xpos2<700 and ypos2+40 >350 and ypos2+40 <570:
        ypos2 = 350-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>500 and xpos2<600 and ypos2+40 >450 and ypos2+40 <470:
        ypos2 = 450-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>500 and xpos2<600 and ypos2+40 >250 and ypos2+40 <270:
        ypos2 = 250-40
        isOnGround2 = True
        vy2 = 0
        
        
        
    else:
    
        isOnGround2 = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
        
    if ypos2 > 760:
        isOnGround2 = True
        vy2 = 0
        ypos2 = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2
        
    if isOnGround2 == False:
        vy2+=.2#notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
    xpos2+=vx2 
    ypos2+=vy2
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    
    pygame.draw.rect(screen, (100, 200, 100), (xpos2, ypos2, 20, 40))
    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))
    
    pygame.draw.rect(screen, (100, 0, 200), (300, 750, 100, 20))
    pygame.draw.rect(screen, (100, 70, 200), (400, 550, 100, 20))
    pygame.draw.rect(screen, (100, 0, 200), (600, 350, 100, 20))
    pygame.draw.rect(screen, (100, 0, 200), (500, 450, 100, 20))
    pygame.draw.rect(screen, (100, 0, 200), (500, 250, 100, 20))
    
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
