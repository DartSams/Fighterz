import pygame

screen_width,screen_height = 1000,600
win = pygame.display.set_mode((screen_width,screen_height)) #inits the game window to set width and height
run = True #variable for game loop
fps = pygame.time.Clock() #inits the game clock all computers will run game at the same speed
level_floor = screen_height - 100 #sets the floor so player doesnt go below it
warrior_sprite_size = 162 #the individual image size (whole sprite sheet is 1620 pixels wide and there are 10 frames for 162 pixel size for 1 image)
wizard_sprite_size = 250 #the individual image size (whole sprite sheet is 1620 pixels wide and there are 10 frames for 162 pixel size for 1 image)
warrior_scale = 4
wizard_scale = 3
warrior_offset = [72,56]
wizard_offset = [112,106]
warrior_data = [warrior_sprite_size,warrior_scale,warrior_offset]
wizard_data = [wizard_sprite_size,wizard_scale,wizard_offset]