# Descripción: Director de creación del mapa
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares
from Project.mapGeneration.MapCreator import MapCreator


class MapDir:

    def __init__(self):
        self.mapCreator = MapCreator()

    def construct(self):
        self.mapCreator.create_map()
        self.mapCreator.build_hollows()
        self.mapCreator.build_doors()
        self.mapCreator.build_obstacles()
        self.mapCreator.build_power_up()

    def set_map_creator(self, creator):
        self.mapCreator = creator

    def get_map(self):
        return self.mapCreator.get_map()
