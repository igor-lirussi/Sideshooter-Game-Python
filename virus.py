import pygame 
from cell import Cell

#inhearitance from Cell class
class Virus(Cell):
    #Constructor with more arguments
    def __init__(self, virus_type, image, position_x, position_y, name="WhiteBloodCell", width=256, speed_x=0, speed_y=0, damage = 10):
        #initialization of properties of the parent Cell class
        super().__init__(image, position_x, position_y, name, width, speed_x, speed_y)
        self.type = virus_type
        self.damage = damage


#inhearitance from Virus class
class Covid_19(Virus):
    def __init__(self, image, position_x, position_y, name="Covid_19", width=256, speed_x=0, speed_y=0, damage = 10):
        super().__init__(image, position_x, position_y, name, width, speed_x, speed_y, damage, virus_type="Covid_19")

class Omicron(Virus):
    def __init__(self, image, position_x, position_y, name="Omicron", width=256, speed_x=0, speed_y=0, damage = 10):
        super().__init__(image, position_x, position_y, name, width, speed_x, speed_y, damage, virus_type="Omicron")

class Delta(Virus):
    def __init__(self, image, position_x, position_y, name="Delta", width=256, speed_x=0, speed_y=0, damage = 10):
        super().__init__(image, position_x, position_y, name, width, speed_x, speed_y, damage, virus_type="Delta")