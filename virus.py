import pygame 


class Virus(Cell):
    def __init__(self):
        super(Virus,self).__init__()
        self.virus_type("image")
class Covid_19(Virus):
    def __init__(self):
        super(Covid_19,self).__init__()
        self.health()
        self.speed()
        self.damage()
class Omicron(Virus):
    def __init__(self):
        super(Omicron,self).__init__()
        self.health()
        self.speed()
        self.damage()
class Delta(Virus):
    def __init__(self):
        super(Delta,self).__init__()
        self.health()
        self.speed()
        self.damage()