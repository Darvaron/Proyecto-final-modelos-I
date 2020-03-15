# Descripción: Builder abstracto del mapa
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC, abstractmethod
from Project.mapGeneration.Map import Map


class MapCreator(ABC):

    def __init__(self):
        self.map = None

    def get_map(self):
        return self.map

    def create_map(self):
        self.map = Map()

    def build_hollows(self):
        pass

    def build_obstacles(self):
        pass

    def build_doors(self, room):
        pass

    def build_power_up(self):
        pass

    def verifier(self):
        pass
