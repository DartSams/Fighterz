import pygame

screen_width,screen_height = 700,500
win = pygame.display.set_mode((screen_width,screen_height)) #inits the game window to set width and height
run = True #variable for game loop
fps = pygame.time.Clock() #inits the game clock all computers will run game at the same speed
level_floor = screen_height - 100 #sets the floor so player doesnt go below it
warrior_sprite_size = 162 #the individual image size (whole sprite sheet is 1620 pixels wide and there are 10 frames for 162 pixel size for 1 image)
wizard_sprite_size = 250 #the individual image size (whole sprite sheet is 1620 pixels wide and there are 10 frames for 162 pixel size for 1 image)
warrior_data = [warrior_sprite_size]
wizard_data = [wizard_sprite_size]