# 1 - Import library
import pygame
import math

from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 0 - Up, 1-Right, 2-Down, 3-Left
keys = [False, False, False, False]
playerpos=[100,100]

# Number of arrows shot successfully, number of arrows shot
accuracy=[0,0]

# Store info about arrows
arrows=[]

# 3 - Load images
player = pygame.image.load("/home/jai/Desktop/skillkidz/session11/game-with-python--main/resources/images/dude.png")
arrow = pygame.image.load("/home/jai/Desktop/skillkidz/session11/game-with-python--main/resources/images/bullet1.png")

# 4 - keep looping through
while True:
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    # 6 - draw the screen elements
    
    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    # atan2 returns the angle in radians, so we use math.degrees to convert it to degrees
    angle = math.degrees(math.atan2(position[1]-playerpos[1], position[0]-playerpos[0]))
    playerrot = pygame.transform.rotate(player, -angle)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(playerpos1[0], playerpos1[1], playerrot.get_rect().width, playerrot.get_rect().height),  2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - Draw arrows
    for bullet in arrows:
        # index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        # if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
        #     arrows.pop(index)
        # index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 

        if event.type==pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_LEFT:
                keys[3] = True  

        if event.type==pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_RIGHT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_LEFT:
                keys[3] = False  
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            accuracy[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

    # 9 - 
    if keys[0]:
        playerpos[1] -= .3
    elif keys[2]:
        playerpos[1] += .3

    if keys[1]:
        playerpos[0] += .3
    elif keys[3]:
        playerpos[0] -= .3
            
