# Descripción: Clase concreta state, todos los enemigos muertos
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from .State import State

class Opened(State):
    def doorAction(self, room, actroom, hollows, displayWidth, displayHeight, act):
        act(hollows, displayWidth, displayHeight)
        return room, None
