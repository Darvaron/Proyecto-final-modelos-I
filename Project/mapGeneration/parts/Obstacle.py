# Descripción: Objetos del entorno
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Obstacle:

    all_obstacles = ['0', '1', '2']

    def __init__(self, hollows, displayWidth, displayHeight):
        self.posx = 0
        self.posy = 0
        self.type = None
        self.image = None
        self.imageWidth = 20
        self.imageHeight = 20
        self.generate_obs(hollows, displayWidth, displayHeight)

    def generate_obs(self, hollows, displayWidth, displayHeight):
        self.posx = random.randint(0, displayWidth - self.imageWidth)
        self.posy = random.randint(0, displayHeight - self.imageHeight)
        pos = Point(self.posx, self.posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        self.type = Obstacle.all_obstacles[random.randint(0, len(Obstacle.all_obstacles) - 1)]
        self.image = pygame.image.load('./resources/obstacles/obstacle_' + self.type + '.png')
        size = self.image.get_rect().size
        self.imageWidth = size[0]
        self.imageHeight = size[1]
        self.image = pygame.transform.scale(self.image, ((round(self.imageWidth / 3)), (round(self.imageHeight / 3))))
        print('Obstaculo:', self.type)

        if not validated:
            self.generate_obs(hollows, displayWidth, displayHeight)
