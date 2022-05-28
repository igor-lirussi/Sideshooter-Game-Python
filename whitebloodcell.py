from cell import Cell

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