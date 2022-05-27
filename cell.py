import pygame
import os

class Cell:
    """ a generic Cell """
    #to initialize the class with arguments, some if not provided are default
    def __init__(self, image, position_x, position_y, name="Cell", health=100, height=256, width=256, speed_x=1, speed_y=1):
        self.image = image
        self.position_x = position_x
        self.position_y = position_y
        self.name = name
        self.health = health
        self.height = height
        self.width = width
        self.speed_x = speed_x
        self.speed_y = speed_y

        #creates surface, loading image, and creating a faster copy considering transparency
        self.player_surf = pygame.image.load(os.path.join('img', self.image)).convert_alpha()
        #scale to desired size
        self.player_surf = pygame.transform.smoothscale(self.player_surf, (self.width, self.height))
        #get rectangle around player, 0,0 512, 512
        #player_rect = player_surf.get_rect()
        #print(player_rect) 

    def draw(self, screen):
        #draw element on screen
        screen.blit(self.player_surf, (self.position_x,self.position_y))

    #MOVEMENT
    def up(self):
        self.position_y = self.position_y - self.speed_y
        if self.position_y<0:
            self.position_y=0

    def down(self):
        self.position_y = self.position_y + self.speed_y
        if self.position_y>pygame.display.get_window_size()[1]-self.height:
            self.position_y=pygame.display.get_window_size()[1]-self.height

    def left(self):
         self.position_x = self.position_x - self.speed_x
         if self.position_x<0:
            self.position_x=0

    def right(self):
        self.position_x = self.position_x + self.speed_x
        if self.position_x>pygame.display.get_window_size()[0]-self.width:
            self.position_x=pygame.display.get_window_size()[0]-self.width


    def kill(self):
        self.health=0
        return "cell killed"
       
    #to print the object
    def __str__(self):
    	return "Cell named '{}' health: {} at: {},{} speed: {},{}".format(self.name,self.health, self.position_x, self.position_y, self.speed_x, self.speed_y)
