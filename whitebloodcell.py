import pygame
from cell import Cell

#inhearitance from Cell class
class WhiteBloodCell(Cell):
	#Constructor with more arguments
    def __init__(self, image, position_x, position_y, name="WhiteBloodCell", width=256, speed_x=0, speed_y=0, speed = 0, health = 100):
    	#initialization of properties of the parent Cell class
    	super().__init__(image, position_x, position_y, name, width, speed_x, speed_y)
    	self.speed = speed
    	self.health = health
        
        