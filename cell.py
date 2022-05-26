import pygame

class Cell:
    #to initialize the class with arguments, some if not provided are default
    def __init__(self, image, position_x, position_y, name="Cell", width=256, speed_x=0, speed_y=0):
        self.name = name
        self.image = image
        self.width = width
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def function(self):
        return "function called"
       
    #to print the object
    def __str__(self):
    	return "Cell '{}' at: {},{} speed: {},{}".format(self.name, self.position_x, self.position_y, self.speed_x, self.speed_y)
