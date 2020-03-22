# Descripción: Mejoras del personaje
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class PowerUp:
    all_Powerups = [['0', 'sword'], ['3', 'hat'], ['4', 'apple']]

    def __init__(self, hollows, displayWidth, displayHeight):
        self.posx = 0
        self.posy = 0
        self.type = None
        self.image = None
        self.power = None
        self.imageWidth = 0
        self.imageHeight = 0
        self.generate_power_up(hollows, displayWidth, displayHeight)

    def generate_power_up(self, hollows, displayWidth, displayHeight):
        self.posx = random.randint(0, displayWidth - self.imageWidth)
        self.posy = random.randint(0, displayHeight - self.imageHeight)
        pos = Point(self.posx, self.posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        self.type = PowerUp.all_Powerups[random.randint(0, len(PowerUp.all_Powerups) - 1)]
        self.power = self.type[1]
        self.image = pygame.image.load('./resources/powerups/Item__' + self.type[0] + '.png')
        size = self.image.get_rect().size
        self.imageWidth = size[0]
        self.imageHeight = size[1]
        self.image = pygame.transform.scale(self.image, ((self.imageWidth * 3), (self.imageHeight * 3)))
        print('PowerUp:', self.power)
        if not validated:
            self.generate_power_up(hollows, displayWidth, displayHeight)
