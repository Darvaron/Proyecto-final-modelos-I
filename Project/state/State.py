# Descripción: Clase abstracta del estado de la puerta
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC, abstractmethod

class State:

    @abstractmethod
    def doorAction(self, room, actroom, hollows, displayWidth, displayHeight, act):
        pass