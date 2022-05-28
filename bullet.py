
class Bullet:
    """ generic bullet """
    def __init__(self, bullet_type, damage, speed = 10):
        self.position_x = position_x
        self.position_y = position_y
        self.bullet_type = bullet_type
        self.damage = damage
        self.speed = speed

    #to print the object
    def __str__(self):
        return "Bullet '{}' damage {} ".format(self.bullet_type, self.damage)
        
    def move_autonomously(self):
        self.position_x=self.position_x+self.speed

class Rocket(Bullet):
    def __init__(self, damage=90):
        super().__init__(bullet_type="Rocket", damage=damage, speed=5)

class NormalBullet(Bullet):
    def __init__(self, damage=10):
        super().__init__(bullet_type="NormalBullet", damage=damage)
        