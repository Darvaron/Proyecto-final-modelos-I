# Descripción: Clase concreta state, enemigos vivos
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from .State import State
import pygame

class Closed(State):

    def doorAction(self, room, actroom, hollows, displayWidth, displayHeight, act):
        image = pygame.image.load('./resources/door/closed.png')
        return actroom, image