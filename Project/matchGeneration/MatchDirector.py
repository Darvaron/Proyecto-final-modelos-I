# Descripción: Director de creación de la partida
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

class MatchDirector:

    def __init__(self):
        self.builder = None

    def defBuilder(self, builder):
        self.builder = builder

    def getMatch(self):
        return self.builder.getMatch()

    def construct(self, displayWidth, displayHeight):
        self.builder.createMatch()
        self.builder.createMaps(displayWidth, displayHeight)
        self.builder.createDoors()
        self.builder.createEnemies(self.builder.getMatch().maps, displayWidth, displayHeight)
        self.builder.createPlayer(self.builder.getMatch().maps, displayWidth, displayHeight)