import pygame
import os
import OOP
from constants import *


#load images
bg = pygame.transform.scale(pygame.image.load("assets/images/background/background.jpg"),(screen_width,screen_height))
#sprite sheet containing all sprite animations
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png")
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png")

#each animation has different number of frames a total of 7 different animation with different number of frames
warrior_animation_steps = [10,8,1,7,7,3,7]
wizard_animation_steps = [8,8,1,8,8,3,7]

#player instance profiles
player1 = OOP.Fighter(win,100,300,warrior_data,warrior_sheet,warrior_animation_steps)
player2 = OOP.Fighter(win,500,300,wizard_data,wizard_sheet,wizard_animation_steps)

#assigns each player a enemy to fight 
player1.enemy = player2
player2.enemy = player1


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
    #draw players health bars
    player1.draw_healthbar(20,20,player1.max_health)
    player2.draw_healthbar(480,20,player2.max_health)
    pygame.display.update()
    fps.tick(60)


pygame.quit()