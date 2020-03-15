# Descripción: Builder concreto de tipo de mapa por defecto
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from Project.mapGeneration.MapCreator import MapCreator
from Project.mapGeneration.parts.Hollow import Hollow
from Project.mapGeneration.parts.Obstacle import Obstacle
from Project.mapGeneration.parts.Door import Door
from Project.mapGeneration.parts.PowerUp import PowerUp
from shapely.geometry.polygon import Polygon


class defaultMap(MapCreator):

    def build_hollows(self):
        quantity = random.randint(0, 2)
        hollows = []
        for n in range(quantity):
            hollows.append(Hollow())
        self.map.set_hollows(hollows)
        print('Hollows creados:', quantity)
        self.verifier(quantity)

    def build_obstacles(self):
        quantity = random.randint(0, 7)
        obs = []
        for n in range(quantity):
            obs.append(Obstacle(self.map.hollows))
        self.map.set_obstables(obs)
        print('Obstaculos creados:', quantity)

    def build_doors(self, room):
        quantity = random.randint(1, 4)
        doors = []
        available = [1, 2, 3, 4]
        for n in range(quantity):
            lane = random.randint(0, len(available)-1)
            pos = available.pop(lane)
            doors.append(Door(pos, room))
        self.map.set_doors(doors)
        print('Puertas generadas:', quantity)

    def build_power_up(self):
        quantity = random.randint(0, 1)
        for n in range(quantity):
            self.map.set_powerups(PowerUp(self.map.hollows))

    def verifier(self, quantity):  # Verifica que los agujeros no se superpongan
        if quantity == 2:
            h1 = self.map.hollows[0]
            h2 = self.map.hollows[1]
            polygon1 = Polygon(h1.corners)
            polygon2 = Polygon(h2.corners)
            if polygon1.intersects(polygon2):
                print('No verificado')
                self.build_hollows()
