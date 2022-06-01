import pygame
from cell import Cell
from colors import Colors

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
        #on the cell 
        #pygame.draw.line(screen, Colors.GREEN, (int(self.position_x), int(self.position_y)), (int(self.position_x + (self.width*(self.health/self.MAX_HEALTH))), int(self.position_y)), 3)
        #on the screen
        window_size=pygame.display.get_window_size()[0]
        health_x1 = window_size/2
        health_y1 = 15
        health_x2 = window_size/6
        health_y2 = 15
        pygame.draw.line(screen, Colors.BLACK, (health_x1 , health_y1), (int(health_x2), health_y2), 20)
        pygame.draw.line(screen, Colors.GREEN, (health_x1 , health_y1), (int(health_x1 - ((health_x1-health_x2)*(self.health/self.MAX_HEALTH))), health_y2), 20)