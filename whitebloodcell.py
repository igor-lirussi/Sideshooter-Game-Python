import pygame
from cell import Cell

GREEN = (0,255, 0)

#inheritance from Cell class
class WhiteBloodCell(Cell):
    """ The player """
    #Constructor 
    def __init__(self, image, position_x, position_y, name="WhiteBloodCell", health=100, height=256, width=256, speed_x=1, speed_y=1):
        #initialization of properties of the parent Cell class
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y)

    def move_autonomously(self):
        #player doesn't need to move autonomously cause it's controlled by events
        pass

    def draw(self, screen):
        super().draw(screen)
        #draw also health
        pygame.draw.line(screen, GREEN, (int(self.position_x), int(self.position_y)), (int(self.position_x + (self.width*(self.health/self.MAX_HEALTH))), int(self.position_y)), 3)