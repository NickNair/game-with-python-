# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100,100]

# 3 - Load images
player = pygame.image.load("/home/jai/Desktop/skillkidz/session11/game-with-python--main/resources/images/dude.png")

# 4 - keep looping through
while True:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, playerpos)
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

    # 9 - 
    if keys[0]:
        playerpos[1] -= .3
    elif keys[2]:
        playerpos[1] += .3

    if keys[1]:
        playerpos[0] += .3
    elif keys[3]:
        playerpos[0] -= .3
