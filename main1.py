import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT,
)
pygame.init()
class Game:
    def __init__(self):
        pass

class Cell:
    def __init__(self):
        pass
class Virus():
    def __init__(self):
        pass
class Covid_19(Virus):
    def __init__(self):
        super(Covid_19,self).__init__()
        pass
class Omicron(Virus):
    def __init__(self):
        super(Omicron,self).__init__()
        pass
class Delta(Virus):
    def __init__(self):
        super(Delta,self).__init__()
        pass
class White_Blood_Cell():
    def __init__(self):
        pass
class Bullet:
    def __init__(self):
        pass
class Booster:
    def __init__(self) -> None:
        pass
class Mask(Booster):
    def __init__(self) -> None:
        super(Booster,self).__init__()
        pass
class Vaccination(Booster):
    def __init__(self) -> None:
        super(Booster, self).__init__()
        pass
class Game:
    self._White_Blood_Cell = White_Blood_Cell()
    self._Virus = Virus()
    self._Mask = Mask()
    self._Vaccination = Vaccination()
    self._Bullet = Bullet()
    self._Covid_19 = Covid_19()
    self._Omicron = Omicron()
    self._Delta = Delta()

    def run_game(self):
        while True:
            break

