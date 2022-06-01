import pygame
import os

class Background():
    #Constructor 
    def __init__(self, image, width, height, speed = 1):
        self.width = width
        self.height = height
        self.speed = speed
        #creates surface, loading image, and creating a faster copy considering transparency (alpha)
        self.surface = pygame.image.load(os.path.join('img', image)).convert_alpha()
        #scale to desired size
        self.surface = pygame.transform.smoothscale(self.surface, (self.width, self.height))
        #rectangle
        self.rect = self.surface.get_rect()

    def move(self):
        self.rect.move_ip(-self.speed,0)

    def draw(self, screen):
        #draw itself on screen
        screen.blit(self.surface, self.rect)
     
    def __str__(self):
        return "Background Image: {}".format(self.surface)
