# Descripción: Director de creación del mapa
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

class MapDir:

    def __init__(self):
        self.mapCreator = None

    def construct(self, room, displayWidth, displayHeight):
        print('Generacion mapa iniciada')
        self.mapCreator.create_map()
        self.mapCreator.build_hollows(displayWidth, displayHeight)
        self.mapCreator.verifier(displayWidth, displayHeight)
        self.mapCreator.build_obstacles(displayWidth, displayHeight)
        self.mapCreator.build_doors(room, displayWidth, displayHeight)
        self.mapCreator.build_power_up(displayWidth, displayHeight)
        self.mapCreator.build_extras()

        print('Mapa generado correctamente')

    def set_map_creator(self, creator):
        self.mapCreator = creator

    def get_map(self):
        return self.mapCreator.get_map()
