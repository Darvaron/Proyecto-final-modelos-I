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
        quantity = random.randint(0, 2)
        hollows = []
        for n in range(quantity):
            hollows.append(Hollow())
        self.map.set_hollows(hollows)
        print('Hollows creados:', quantity)

    def build_obstacles(self):
        quantity = random.randint(0, 7)
        obs = []
        for n in range(quantity):
            obs.append(Obstacle(self.map.hollows))
        self.map.set_obstables(obs)
        print('Obstaculos creados:', quantity)

    def build_doors(self):
        quantity = random.randint(1, 5)
        doors = []
        for n in range(quantity):
            doors.append(Door())
        self.map.set_doors(doors)
        print('Puertas generadas:', quantity)

    def build_power_up(self):
        quantity = random.randint(0, 2)
        for n in range(quantity):
            self.map.set_powerups(PowerUp(self.map.hollows))
