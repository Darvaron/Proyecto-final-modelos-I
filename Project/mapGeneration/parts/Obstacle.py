# Descripción: Objetos del entorno
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
import Project.Main
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Obstacle:

    def __init__(self, hollows):
        self.posx = 0
        self.posy = 0
        self.type = None
        self.generate_obs(hollows)

    def generate_obs(self, hollows):
        posx = random.randint(0, Project.Main.displayWidth + 1)
        posy = random.randint(0, Project.Main.displayHeight + 1)
        pos = Point(posx,posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        if not validated:
            self.generate_obs(hollows)

