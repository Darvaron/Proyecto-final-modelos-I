# Descripción: Clase fabrica factory method
# Autores: David Armando Rodríguez Varón

from .Apple import Apple
from .Hat import Hat
from .Sword import Sword


class PowerUpFactory():

    def __init__(self):
        self.powerup = None

    def get_powerUp(self, case, hollows, displayWidth, displayHeight):
        if case == None:
            return None
        elif case == 'hat':
            return Hat(hollows, displayWidth, displayHeight)
        elif case == 'apple':
            return Apple(hollows, displayWidth, displayHeight)
        else:
            return Sword(hollows, displayWidth, displayHeight)
