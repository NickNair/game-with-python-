# 1 - Import library
import math
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos=[100,100]

arrows = []


# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
arrow =  pygame.image.load("resources/images/bullet.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill((255,255,255))


    # 6 - draw the screen elements
    position = pygame.mouse.get_pos()

    
    
    centre = [ playerpos[0] + 32 , playerpos[1] + 26 ]

    angle = math.degrees( math.atan2( position[1] - centre[1] , position[0] - centre[0] ) )

    playerrot = pygame.transform.rotate( player , 360 - angle )

    playerpos1 = [playerpos[0] - playerrot.get_rect().width//2 ,
                  playerpos[1] - playerrot.get_rect().height//2 ]

    pygame.draw.rect( screen, (255,0,0)  , [playerpos1[0],playerpos1[1],
                                            playerrot.get_rect().width,
                                            playerrot.get_rect().height ] , 1 )
       
    screen.blit(playerrot , playerpos1)

    if arrows != []:

        arrows[1]+=1
        arrows[2]+=-0.1

        screen.blit(arrow,[arrows[1],arrows[2]])
        if arrows[1]>640 or arrows[2]>480:
            arrows=[]
        


    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type== pygame.MOUSEBUTTONDOWN:
            print("Mouse is down")
            position = pygame.mouse.get_pos()
            centre = [ playerpos[0] + 32 , playerpos[1] + 26 ]
            angle = math.degrees( math.atan2( position[1] - centre[1] , position[0] - centre[0] ) )
            
            arrows =[ angle, playerpos[0], playerpos[1] ]




        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False

        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        # 9 - Move player
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    
