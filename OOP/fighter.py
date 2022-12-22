import pygame
from constants import *

class Fighter:
    def __init__(self,win,x,y):
        self.win = win
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.vel = 5
        self.gravity_vel = 4
        self.jump = True
        self.attack_type = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x >= 0: #move left and stay on screen
            self.x -= self.vel
        if keys[pygame.K_d] and self.x + self.width <= screen_width: #move right and stay on screen
            self.x += self.vel

        if keys[pygame.K_w] and self.jump == True: #jump
            self.y -= self.vel * 20
            self.jump = False #turns jump ability off so player doesnt spam jump

        if keys[pygame.K_s] and self.y <= level_floor: #move down and stay on screen
            self.y += self.vel

        if self.y <= level_floor: #applies gravity to player when not touching the floor or jumping
            self.y += self.gravity_vel

        if self.y >= level_floor: #checks if player is touching the floor
            self.jump = True

        ##attack controls keys o and p
        if keys[pygame.K_o] or keys[pygame.K_p]: #checks if keys o or p have been pressed
            
            if keys[pygame.K_o]: #basic attack
                self.attack_type = 1

            if keys[pygame.K_p]: #special attack
                self.attack_type = 2

            self.attack(self.attack_type)

    def attack(self,type): #draws attack radius according to type 
        self.attack_rect = pygame.draw.rect(self.win,(255,0,0),pygame.Rect(self.x+self.width,self.y,self.width,self.height))


    def draw(self):
        self.rect = pygame.draw.rect(self.win,(0,255,0),pygame.Rect(self.x,self.y,self.width,self.height))