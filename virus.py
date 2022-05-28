from cell import Cell

#inheritance from Cell class
class Virus(Cell):
    #Constructor with more arguments
    def __init__(self, virus_type, image, position_x, position_y, name="Virus", health=50, height=256, width=256, speed_x=10, speed_y=10, damage=10):
        #initialization of properties of the parent Cell class
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y)
        #viruses have also type and damage properties
        self.virus_type = virus_type
        self.damage = damage
        #save the initial creation position
        self.initial_pos_x = position_x
        self.initial_pos_y = position_y

    def move_autonomously(self):
        #move left
        self.position_x=self.position_x-self.speed_x
        #if out of the screen
        if self.position_x<0:
            #move back to initial position
            self.position_x = self.initial_pos_x
            self.position_y = self.initial_pos_y

    def __str__(self):
        #string returned from the parent constructor plus the new properties
        return super().__str__() + " virus type: {} damage: {}".format(self.virus_type, self.damage)

#inheritance from Virus class, name can be changed from the default one, virus_type is fixed
class Covid19(Virus):
    def __init__(self, image, position_x, position_y, name="Covid19", health=70, height=256, width=256, speed_x=0, speed_y=0, damage=10):
        super().__init__(virus_type="Covid19", image=image, position_x=position_x, position_y=position_y, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y, damage=damage)

class Omicron(Virus):
    def __init__(self, image, position_x, position_y, name="Omicron", health=80, height=256, width=256, speed_x=0, speed_y=0, damage=20):
        super().__init__(virus_type="Omicron", image=image, position_x=position_x, position_y=position_y, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y, damage=damage)

class Delta(Virus):
    def __init__(self, image, position_x, position_y, name="Delta", health=90, height=256, width=256, speed_x=0, speed_y=0, damage=30):
        super().__init__(virus_type="Delta", image=image, position_x=position_x, position_y=position_y, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y, damage=damage)