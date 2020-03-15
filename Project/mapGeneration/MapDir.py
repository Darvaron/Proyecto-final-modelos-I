# Descripción: Director de creación del mapa
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.mapGeneration.MapCreator import MapCreator


class MapDir:

    def __init__(self):
        self.mapCreator = None

    def construct(self, room):
        print('Generacion mapa iniciada')
        self.mapCreator.create_map()
        self.mapCreator.build_hollows()
        self.mapCreator.build_obstacles()
        self.mapCreator.build_doors(room)
        self.mapCreator.build_power_up()
        print('Mapa generado correctamente')

    def set_map_creator(self, creator):
        self.mapCreator = creator

    def get_map(self):
        return self.mapCreator.get_map()
