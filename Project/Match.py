# Descripción: Clase partida
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from Project.mapGeneration.MapDir import MapDir
from Project.mapGeneration.concreteMapsCreators.defaultMap import defaultMap


class Match:

    def __init__(self):
        self.map = []
        self.generate_match()

    def generate_match(self):
        quantity = random.randint(1, 11)
        for n in range(quantity):
            # Mapa generado mediante builder
            mapDirector = MapDir()
            mapDirector.set_map_creator(defaultMap())
            mapDirector.construct()
            self.map.append(mapDirector.get_map())
            print('Sala', n, 'generada')