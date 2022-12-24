import pygame
from constants import *

class Fighter:
    def __init__(self,win,x,y):
        self.win = win
        self.x = x
        self.y = y
        self.width = 50
        self.height = 150
        self.max_health = 100 #sets a placeholder for max health of player
        self.health = self.max_health #inits the current health of the player to the placeholder original health (this is current so it changes)
        self.vel = 5
        self.gravity_vel = 4
        self.jump = True
        self.attacking = False
        self.attack_type = 0 
        self.enemy = None #gets the enemy object to be used to check collision 


    def draw_healthbar(self,x,y,health):
        pygame.draw.rect(self.win,(255,0,0),(x,y,health*2,30))
        pygame.draw.rect(self.win,(0,255,0),(x,y,self.health*2,30))

    def move(self):
        keys = pygame.key.get_pressed()

        if self.attacking == False: #can only do other actions when not attacking
            if keys[pygame.K_a] and self.x >= 0: #move left and stay on screen
                self.x -= self.vel
            if keys[pygame.K_d] and self.x + self.width <= screen_width: #move right and stay on screen
                self.x += self.vel

            if keys[pygame.K_w] and self.jump == True: #jump
                self.y -= self.vel * 20
                self.jump = False #turns jump ability off so player doesnt spam jump

            if keys[pygame.K_s] and self.y <= level_floor: #move down and stay on screen
                self.y += self.vel

            if self.y + self.height <= level_floor: #applies gravity to player when not touching the floor or jumping
                self.y += self.gravity_vel

            if self.y >= level_floor: #checks if player is touching the floor
                self.jump = True

            ##attack controls keys o and p
            if keys[pygame.K_o] or keys[pygame.K_p]: #checks if keys o or p have been pressed
                self.attacking = True #sets attacking variable to True so player can attack
                if keys[pygame.K_o]: #basic attack
                    self.attack_type = 1

                if keys[pygame.K_p]: #special attack
                    self.attack_type = 2

                self.attack(self.attack_type)

    def attack(self,type): #draws attack radius according to type 
        self.attack_rect = pygame.draw.rect(self.win,(255,0,0),pygame.Rect(self.x+self.width,self.y,self.width,self.height))
        if self.attack_rect.colliderect(self.enemy.rect):
            print("enemy hit")
            self.enemy.health -= 10
            print(self.enemy.health)
            # self.attacking = False

    def draw(self):
        self.rect = pygame.draw.rect(self.win,(0,255,0),pygame.Rect(self.x,self.y,self.width,self.height))  
