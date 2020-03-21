# Descripción: Clase que contiene todos los datos de la partida
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

class Match:

    def __init__(self):
        self.maps = []
        self.doors = []
        self.enemies = []
        self.player = None

    def setMaps(self, maps):
        self.maps = maps

    def setDoors(self, doors):
        self.doors = doors

    def setEnemies(self, enemies):
        self.enemies = enemies

    def setPlayer(self, player):
        self.player = player

