import pygame
import os
import OOP
from constants import *


#load images
bg = pygame.transform.scale(pygame.image.load("assets/images/background/background.jpg"),(screen_width,screen_height))


#player instance profiles
player1 = OOP.Fighter(win,300,400)

player2 = OOP.Fighter(win,300,400)

#game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    win.blit(bg,(0,0))
    player1.draw() #draws player to screen
    player2.draw()
    player1.move() #controls for player movement
    pygame.display.update()
    fps.tick(60)


pygame.quit()