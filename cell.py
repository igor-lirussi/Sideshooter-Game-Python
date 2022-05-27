import pygame
import os

class Cell:
    """ a generic Cell """
    #to initialize the class with arguments, some if not provided are default
    def __init__(self, image, position_x, position_y, name="Cell", health = 100, width=256, speed_x=0, speed_y=0):
        self.name = name
        self.health = health
        self.image = image
        self.width = width
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = speed_y

        #creates surface, loading image, and creating a faster copy considering transparency
        self.player_surf = pygame.image.load(os.path.join('img', self.image)).convert_alpha()
        #scale to desired size
        self.player_surf = pygame.transform.smoothscale(self.player_surf, (self.width, self.width))
        #get rectangle around player, 0,0 512, 512
        #player_rect = player_surf.get_rect()
        #print(player_rect) 

    def draw(self, screen):
        #draw player on screen
        screen.blit(self.player_surf, (self.position_x,self.position_y) )

    def kill(self):
        self.health=0
        return "cell killed"
       
    #to print the object
    def __str__(self):
    	return "Cell named '{}' health: {} at: {},{} speed: {},{}".format(self.name,self.health, self.position_x, self.position_y, self.speed_x, self.speed_y)
