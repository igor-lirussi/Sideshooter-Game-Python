import pygame 
from cell import Cell

#inhearitance from Cell class
class Virus(Cell):
    #Constructor with more arguments
    def __init__(self, virus_type, image, position_x, position_y, name="Virus", health=50, width=256, speed_x=0, speed_y=0, damage=10):
        #initialization of properties of the parent Cell class
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health= health, width=width, speed_x=speed_x, speed_y=speed_y)
        #viruses have also type and damage properties
        self.virus_type = virus_type
        self.damage = damage

    #to print the object
    def __str__(self):
        #string returned from the parent constructor plus the new properties
        return super().__str__() + " virus type: {} damage: {}".format(self.virus_type, self.damage)

#inhearitance from Virus class, name can be changed from the default one, virus_type is fixed
class Covid19(Virus):
    def __init__(self, image, position_x, position_y, name="Covid19", health=70, width=256, speed_x=0, speed_y=0, damage=10):
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health=health, width=width, speed_x=speed_x, speed_y=speed_y, damage=damage, virus_type="Covid19")

class Omicron(Virus):
    def __init__(self, image, position_x, position_y, name="Omicron", health=80, width=256, speed_x=0, speed_y=0, damage=20):
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health=health, width=width, speed_x=speed_x, speed_y=speed_y, damage=damage, virus_type="Omicron")

class Delta(Virus):
    def __init__(self, image, position_x, position_y, name="Delta", health=90, width=256, speed_x=0, speed_y=0, damage=30):
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health=health, width=width, speed_x=speed_x, speed_y=speed_y, damage=damage, virus_type="Delta")