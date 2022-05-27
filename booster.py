
class Booster:
    """ generic powerup """
    def __init__(self, booster_type, health_increase, collision_protection_time):
        self.booster_type = booster_type
        self.health_increase = health_increase
        self.collision_protection_time = collision_protection_time

    #to print the object
    def __str__(self):
        return "Booster '{}' increasing {} and protecting for {}".format(self.booster_type, self.health_increase, self.collision_protection_time)
        
        

class Mask(Booster):
    """ has more protection time than health increase"""
    def __init__(self, health_increase=10, collision_protection_time=10):
        super().__init__(booster_type="Mask", health_increase=health_increase, collision_protection_time=collision_protection_time)

class Vaccination(Booster):
    """ has more health increase """
    def __init__(self, health_increase=90, collision_protection_time=5):
        super().__init__(booster_type="Vaccination", health_increase=health_increase, collision_protection_time=collision_protection_time)
        