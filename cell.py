import pygame
import os

class Cell(pygame.sprite.Sprite):
    """ a generic Cell in the human body, a base game object. Image and Postions are required """
    #to initialize the class with arguments, some if not provided are default
    def __init__(self, image, position_x, position_y, name="Cell", health=100, height=256, width=256, speed_x=1, speed_y=1):
        super().__init__() 
        self.image = image
        self.position_x = position_x
        self.position_y = position_y
        self.name = name
        self.health = health
        self.MAX_HEALTH = health
        self.height = height
        self.width = width
        self.speed_x = speed_x
        self.speed_y = speed_y

        #creates surface, loading image, and creating a faster copy considering transparency (alpha)
        self.cell_surface = pygame.image.load(os.path.join('img', self.image)).convert_alpha()
        #scale to desired size
        self.cell_surface = pygame.transform.smoothscale(self.cell_surface, (self.width, self.height))
        #get rectangle around for collision detection es:<rect(0, 0, 60, 60)>
        #has to be called "rect"
        self.rect = self.cell_surface.get_rect()
        #move the rectangle to the current position of the obj
        self.rect.update(self.position_x, self.position_y,self.width, self.height)
        #print(self.rect) 

    def update_rect(self):
        self.rect.update(self.position_x, self.position_y,self.width, self.height)


    def draw(self, screen):
        #draw itself on screen
        screen.blit(self.cell_surface, (self.position_x,self.position_y))

    def get_position(self):
        return (self.position_x, self.position_y)

    def set_position(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    #MOVEMENT 
    #moves the cell, player or enemy to a direction, within the screen
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

    def move_autonomously(self):
        print("move_autonomously not implemented")
        #to be overridden

    def kill(self):
        self.health=0
        return "cell killed"
       
    #to print the object
    def __str__(self):
    	return "Cell named '{}' at: {},{} health: {} speed: {},{}".format(self.name, self.position_x, self.position_y, self.health, self.speed_x, self.speed_y)
