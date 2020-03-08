# Descripción: Clase partida
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.mapGeneration.MapDir import MapDir
from Project.mapGeneration.concreteMapsCreators.defaultMap import defaultMap
from Project.mapGeneration.Map import Map


class Match:

    def __init__(self):
        self.map = None
        self.generate_match()

    def generate_match(self):
        # Mapa generado mediante builder
        mapDirector = MapDir()
        mapDirector.set_map_creator(defaultMap())
        mapDirector.construct()
        self.map = mapDirector.get_map()