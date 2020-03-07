# Descripción: Builder concreto de tipo de mapa por defecto
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from Project.mapGeneration.MapCreator import MapCreator
from Project.mapGeneration.parts.Hollow import Hollow
from Project.mapGeneration.parts.Obstacle import Obstacle
from Project.mapGeneration.parts.Door import Door
from Project.mapGeneration.parts.PowerUp import PowerUp


class defaultMap(MapCreator):

    def build_hollows(self):
        quantity = random.randint(0, 5)
        for n in range(quantity):
            MapCreator.map.hollows.append(Hollow())

    def build_obstacles(self):
        quantity = random.randint(0, 7)
        for n in range(quantity):
            MapCreator.map.obstacles.append(Obstacle(MapCreator.map.hollows))

    def build_doors(self):
        quantity = random.randint(1, 5)
        for n in range(quantity):
            MapCreator.map.doors.append(Door())

    def build_power_ups(self):
        quantity = random.randint(0, 2)
        for n in range(quantity):
            MapCreator.map.powerUps = PowerUp()
