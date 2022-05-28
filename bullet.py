from cell import Cell
from enum import Enum
import pygame

class Status(Enum):
    FIRED = 1
    READY = 2

class Bullet(Cell):
    """ generic bullet """
    #Constructor 
    def __init__(self, bullet_type, damage, image, position_x, position_y, status=Status.READY, name="Bullet", health=100, height=256, width=256, speed_x=1, speed_y=1):
        #initialization of properties of the parent Cell class
        super().__init__(image=image, position_x=position_x, position_y=position_y, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y)
        self.bullet_type = bullet_type
        self.damage = damage
        self.status = status
        #save the initial creation position
        self.initial_pos_x = position_x
        self.initial_pos_y = position_y

    def __str__(self):
        #string returned from the parent constructor plus the new properties
        return super().__str__() + " Bullet type '{}' damage {} ".format(self.bullet_type, self.damage)
        
    def move_autonomously(self):
        if self.status == Status.FIRED:
            #move right
            self.position_x=self.position_x+self.speed_x
        #if out of the screen
        if self.position_x > pygame.display.get_window_size()[0]:
            self.status = Status.READY
            #move back to initial position
            self.position_x = self.initial_pos_x
            self.position_y = self.initial_pos_y

    def fire(self, position_x, position_y):
        self.status = Status.FIRED
        self.position_x = position_x
        self.position_y = position_y

    def is_ready(self):
        return self.status == Status.READY

class Rocket(Bullet):
    def __init__(self, image, position_x, position_y, damage=90, status=Status.READY, name="Rocket", health=100, height=256, width=256, speed_x=1, speed_y=1):
        super().__init__(bullet_type="Rocket", damage=damage, image=image, position_x=position_x, position_y=position_y, status = status, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y)

class NormalBullet(Bullet):
    def __init__(self, image, position_x, position_y, damage=10, status=Status.READY, name="NormalBullet", health=100, height=256, width=256, speed_x=5, speed_y=5):
        super().__init__(bullet_type="NormalBullet", damage=damage, image=image, position_x=position_x, position_y=position_y, status = status, name=name, health=health, height=height, width=width, speed_x=speed_x, speed_y=speed_y)
        
