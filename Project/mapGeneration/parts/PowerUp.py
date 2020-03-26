# Descripción: Mejoras del personaje
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from abc import ABC, abstractmethod


class PowerUp:

    # all_Powerups = [['0', 'sword'], ['3', 'hat'], ['4', 'apple']]

    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.type = None
        self.image = None
        self.power = None
        self.imageWidth = 0
        self.imageHeight = 0
        #self.generate_power_up(hollows, displayWidth, displayHeight)

    def validate(self, hollows, posx, posy):
        pos = Point(posx, posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        return validated

    @abstractmethod
    def generate_power_up(self):
        pass