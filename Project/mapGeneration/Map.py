# Descripción: Mapa compuesto de agujeros, obstaculos, puertas y mejoras
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

class Map:

    def __init__(self):
        self.hollows = []
        self.obstacles = []
        self.doors = []
        self.powerUps = None

    def set_hollows(self, hollows):
        self.hollows = hollows

    def set_obstables(self, obstacles):
        self.obstacles = obstacles

    def set_doors(self, doors):
        self.doors = doors

    def set_powerups(self, powerUps):
        self.powerUps = powerUps
