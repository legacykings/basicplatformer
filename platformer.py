import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
from winsound import Beep

Link = pygame.image.load('link.png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

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
ypos = 600 #ypos of player
xpos2 = 400 #xpos of player
ypos2 = 600 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
vx2 = 0 #x velocity of player
vy2 = 0 
keys = [False, False, False, False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
isOnGround2 = False
health = 100
health2 = 100

enemy1 = [600, 330, 0] 
enemy2 = [500, 430, 10]
enemy3 = [100, 710, 50 ]

def enemyMove(enemyInfo):
    enemyInfo[2]+=1
    if enemyInfo[2] <= 40:
        enemyInfo[0] += 1
    elif enemyInfo[2] <= 80:
        enemyInfo[0] -=1
    else:
        enemyInfo[2] = 0 #reset timer

def enemyMove2(enemyInfo):
    enemyInfo[2]+=1
    if enemyInfo[2] <= 30:
        enemyInfo[1] += 1
    elif enemyInfo[2] <= 60:
        enemyInfo[1] -=1
    else:
        enemyInfo[2] = 0 #reset timer
       
def enemyCollide(enemyInfo, playerX, playerY):
    if playerX+64>enemyInfo[0]: #right side of player, left side of enemy
        if playerX < enemyInfo[0]+20: #left sdie of player, right side of enemy
            if playerY < enemyInfo[1]+96: #top of the player, bottom of the enemy
                if playerY+96 > enemyInfo[1]:
                    return True
    else:
        return False
def enemyCollide2(enemyInfo, playerX, playerY):
    if playerX+20>enemyInfo[0]: #right side of player, left side of enemy
        if playerX < enemyInfo[0]+20: #left sdie of player, right side of enemy
            if playerY < enemyInfo[1]+40: #top of the player, bottom of the enemy
                if playerY+40 > enemyInfo[1]:
                    return True
    else:
        return False

frameWidth = 64
frameHeight = 96
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

background = pygame.image.load("sebastian2.png")


while not gameover and health > 0: #GAME LOOP############################################################
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
                Beep(500, 50)
            elif event.key == pygame.K_a:
                keys[a]=True
            elif event.key == pygame.K_d:
                keys[d]=True
            elif event.key == pygame.K_w:
                keys[w]=True
                Beep(500, 50)
                
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
        vx=-7
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=+7
        direction = RIGHT
    elif keys[a]==True:
        vx2=-8
       
    elif keys[d]==True:
        vx2=+8
       

    #turn off velocity
    else:
        vx = 0
        vx2 = 0
        
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -9
        isOnGround = False
        direction = UP
    elif keys[w] == True and isOnGround2 == True: #only jump when on the ground
        vy2 = -9
        isOnGround2 = False
        direction = UP
        
    enemyMove(enemy1)

       
    enemyMove(enemy2)
   
   
    enemyMove2(enemy3)
    
    
    if enemyCollide(enemy1, xpos, ypos):
        print("hit")
        health  -=10
    if enemyCollide(enemy2, xpos, ypos):
        print("hit")
        health  -=10
    if enemyCollide(enemy3, xpos, ypos):
        print("hit")
        health  -=10
    
    if enemyCollide2(enemy1, xpos2, ypos2):
        print("hit")
        health  -=10
    if enemyCollide2(enemy2, xpos2, ypos2):
        print("hit")
        health  -=10
    if enemyCollide2(enemy3, xpos2, ypos2):
        print("hit")
        health  -=10
    
    

    
    #COLLISION
    if xpos>40 and xpos<200 and ypos+96 >750 and ypos+96 <814:
        ypos = 750-96
        isOnGround = True
        vy = 0
    elif xpos>140 and xpos<300 and ypos+96 >650 and ypos+96 <714:
        ypos = 650-96
        isOnGround = True
        vy = 0
    elif xpos>240 and xpos<400 and ypos+96 >750 and ypos+96 <814:
        ypos = 750-96
        isOnGround = True
        vy = 0
    elif xpos>340 and xpos<500 and ypos+96 >550 and ypos+96 <614:
        ypos = 550-96
        isOnGround = True
        vy = 0
    elif xpos>540 and xpos<700 and ypos+96 >350 and ypos+96 <414:
        ypos = 350-96
        isOnGround = True
        vy = 0
    elif xpos>440 and xpos<600 and ypos+96 >450 and ypos+96 <514:
        ypos = 450-96
        isOnGround = True
        vy = 0
    elif xpos>440 and xpos<600 and ypos+96 >250 and ypos+96 <314:
        ypos = 250-96
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
    if ypos > 700:
        isOnGround = True
        vy = 0
        ypos = 700
        
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
    
    
    
    if vx < 0: 
        RowNum = 0 
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>7:
           frameNum = 0
           
    if vx > 0: 
        RowNum = 1 
        ticker+=1
        if ticker%10==0: 
          frameNum+=1         
        if frameNum>7:
           frameNum = 0
           
    if vy < 0: 
        RowNum = 2 
        ticker+=1
        if ticker%10==0: 
          frameNum+=1          
        if frameNum>7:
           frameNum = 0
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    screen.blit(background, (00,00))
  
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    
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
    pygame.draw.rect(screen, (255,255,255), (enemy1[0], enemy1[1], 20, 20)) #access first and second slot of LIST
    pygame.draw.rect(screen, (255,255,255), (enemy2[0], enemy2[1], 20, 20))
    pygame.draw.rect(screen, (255,255,255), (enemy3[0], enemy3[1], 20, 20))
    
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
if health <=0:
    print("game over, you died")
pygame.quit()
