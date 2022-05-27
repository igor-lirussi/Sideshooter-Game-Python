import pygame
from cell import Cell

#inheritance from Cell class
class WhiteBloodCell(Cell):
	#Constructor with more arguments
    def __init__(self, image, position_x, position_y, name="WhiteBloodCell", health=100, width=256, speed_x=0, speed_y=0):
    	#initialization of properties of the parent Cell class
    	super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health= health, width=width, speed_x=speed_x, speed_y=speed_y)
        
        