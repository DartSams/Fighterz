import pygame

screen_width,screen_height = 700,500
win = pygame.display.set_mode((screen_width,screen_height)) #inits the game window to set width and height
run = True #variable for game loop
fps = pygame.time.Clock() #inits the game clock all computers will run game at the same speed
level_floor = screen_height - 100 #sets the floor so player doesnt go below it