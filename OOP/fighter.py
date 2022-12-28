import pygame
from constants import *

class Fighter:
    def __init__(self,win,x,y,data,sheet,animation_steps):
        self.win = win
        self.x = x
        self.y = y
        self.sprite_sheet = sheet
        self.animation_steps = animation_steps
        self.sprite_size = data[0] #pixel size of sprite
        self.image_scale = data[1]
        self.image_offset = data[2]
        self.width = 100
        self.height = 150
        self.max_health = 100 #sets a placeholder for max health of player
        self.health = self.max_health #inits the current health of the player to the placeholder original health (this is current so it changes)
        self.vel = 5
        self.gravity_vel = 4
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0 
        self.enemy = None #gets the enemy object to be used to check collision 
        self.flip = False #check the position of the facing player returns a 0 or 1
        self.animation_dict = self.load_images() #dict containing all spirte animations list 
        self.action = 0 #0:idle,1:run,2:jump,3:attack1,4:attack2,5:hit,6:death
        self.animation_names = {
            "0":"idle",
            "1":"run",
            "2":"jump",
            "3":"attack1",
            "4":"attack2",
            "5":"hit",
            "6":"death"
        } #defines animation name for individual animations
        self.frame_index = 0 #what frame to start the image on
        self.image = self.animation_dict[self.animation_names[str(self.action)]][self.frame_index] #returns the image from the animation list
        self.update_image = pygame.time.get_ticks() #creates a timestamp of first called


    def draw_healthbar(self,x,y,health):
        pygame.draw.rect(self.win,(255,0,0),(x,y,health*2,30))
        pygame.draw.rect(self.win,(0,255,0),(x,y,self.health*2,30))

    def move(self):
        keys = pygame.key.get_pressed()
        self.running = False
        # self.update_action(0)
        # self.action = 0 #makes the current animation action to idle 

        # if self.enemy.x > self.x: #checks if enemy is to the right of the player
        #     self.flip = False
        # else: #if enemy is to the left of the player toggles variable so player faces the other way
        #     self.flip = True

        if self.attacking == False: #can only do other actions when not attacking
            if keys[pygame.K_a] and self.x >= 0: #move left and stay on screen
                self.x -= self.vel
                self.running = True
                # self.update_action(1) #makes the current animation action to run
                # self.action = 1
                self.flip = True

            if keys[pygame.K_d] and self.x + self.width <= screen_width: #move right and stay on screen
                self.x += self.vel
                self.running = True
                # self.update_action(1) #makes the current animation action to run
                # self.action = 1

            if keys[pygame.K_w] and self.jump == False: #jump
                self.y -= 90
                self.jump = True #turns jump ability off so player doesnt spam jump
                # self.update_action(2) #makes the current animation action to jump
                # self.action = 2

            if keys[pygame.K_s] and self.y <= level_floor: #move down and stay on screen
                pass
                # self.y += self.vel

            # if self.y + self.height <= level_floor: #applies gravity to player when not touching the floor or jumping
            #     self.y += self.gravity_vel

            # if self.y + self.height >= level_floor: #checks if player is touching the floor
            #     self.jump = True

            ##attack controls keys o and p
            if keys[pygame.K_o] or keys[pygame.K_p]: #checks if keys o or p have been pressed
                self.attacking = True #sets attacking variable to True so player can attack
                if keys[pygame.K_o]: #basic attack
                    self.attack_type = 1
                    # self.update_action(3) #makes the current animation action to attack 1
                    # self.action = 3

                if keys[pygame.K_p]: #special attack
                    self.attack_type = 2
                    # self.update_action(4) #makes the current animation action to attack 2
                    # self.action = 4 

                self.attack(self.attack_type)

    def update_action(self,new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0

            self.update_image = pygame.time.get_ticks()

    def update(self): #0:idle,1:run,2:jump,3:attack1,4:attack2,5:hit,6:death
        if self.running == True:
            self.update_action(1)
        elif self.jump == True:
            self.update_action(2)
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)   
        else:
            self.update_action(0)


        animation_cooldown = 50 #timer for how each animation frame will take (so 50 milliseconds the lower the smoother)
        # self.image = self.animation_dict[self.animation_names[str(self.action)]][self.frame_index] #returns the image from the animation list
        if pygame.time.get_ticks() - self.update_image > animation_cooldown and len(self.animation_dict[self.animation_names[str(self.action)]]) > 1: 
            self.frame_index += 1 #cycles through the frames of a animation
            self.update_image = pygame.time.get_ticks()


        if self.frame_index >= len(self.animation_names[str(self.action)]): #checks if frame index has reached the last frame in the animation list
            self.frame_index = 0 #resets frame index back to 0 to start animation over
            if self.attacking: #toggles attack to off so not stuck in a attacking loop
                self.attacking = False
        else:
            self.image = self.animation_dict[self.animation_names[str(self.action)]][self.frame_index] #returns the image from the animation list

    def attack(self,type): #draws attack radius according to type 
        self.attack_rect = pygame.draw.rect(self.win,(255,0,0),pygame.Rect(self.x+self.width - (2 * self.width * self.flip),self.y,self.width,self.height)) #{self.x+self.width - (2 * self.width * self.flip)} sets the x of the attacking hitbox to be the direction of the player facing if self.flip = False then its being mutplied by 0 so player is facing to the right
        if self.attack_rect.colliderect(self.enemy.rect):
            # print("enemy hit")
            self.enemy.health -= 10
            # print(self.enemy.health)
            # self.attacking = False #needs to be placed where after attacking can toggle back off

    def draw(self):
        self.update()
        flip_img = pygame.transform.flip(self.image,self.flip,False) #flips image according to the x axis
        self.rect = pygame.draw.rect(self.win,(0,255,0),pygame.Rect(self.x,self.y,self.width,self.height))  
        self.win.blit(flip_img,(self.x - (self.image_offset[0] * self.image_scale),self.y - (self.image_offset[1] * self.image_scale))) #draws the image on top of the rect

        if self.y + self.height <= level_floor: #applies gravity to player when not touching the floor or jumping
            self.y += self.gravity_vel

        if self.y + self.height >= level_floor: #checks if player is touching the floor
            self.jump = False

        if self.enemy.x > self.x: #checks if enemy is to the right of the player
            self.flip = False
        else: #if enemy is to the left of the player toggles variable so player faces the other way
            self.flip = True


    def load_images(self): #loads individual animations #0:idle,1:run,2:jump,3:attack1,4:attack2,5:hit,6:death
        animation_names = {
            "0":"idle",
            "1":"run",
            "2":"jump",
            "3":"attack1",
            "4":"attack2",
            "5":"hit",
            "6":"death"
        } #defines animation name for individual animations
        # animation_lst = []
        animation_dict = {}
        for y,animation in enumerate(self.animation_steps): #loops through all 
            temp_img_lst = []
            for x in range(animation): #loops throught the images left to right
                temp_img = self.sprite_sheet.subsurface(x * self.sprite_size,y * self.sprite_size,self.sprite_size,self.sprite_size) #subsurface grabs a area around a image given the coordinates 
                scaled_image = pygame.transform.scale(temp_img,(self.sprite_size * self.image_scale,self.sprite_size * self.image_scale))
                temp_img_lst.append(scaled_image)
            # animation_lst.append(temp_img_lst)
            animation_dict[animation_names[str(y)]] = temp_img_lst
        # print(animation_dict)
        return animation_dict