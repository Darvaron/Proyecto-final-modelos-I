# Descripción: Creador abstracto de match
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import abstractmethod, ABC
from Project.matchGeneration.Match import Match


class MatchBuilder(ABC):

    def __init__(self):
        self.match = None

    def getMatch(self):
        return self.match

    def createMatch(self):
        self.match = Match()

    @abstractmethod
    def createMaps(self, displayWidth, displayHeight):
        pass

    @abstractmethod
    def createDoors(self):
        pass

    @abstractmethod
    def createEnemies(self, maps, displayWidth, displayHeight):
        pass

    @abstractmethod
    def createPlayer(self, maps, displayWidth, displayHeight):
        pass

    @staticmethod
    def delete_empty(self):  # Elimina salas sin puertas
        pos = 0
        eliminated = 0
        for m in self.match.map:
            hasDoors = False
            for d in self.doors:
                if d.room == m.id:
                    hasDoors = True
            if not hasDoors:
                print('Eliminando sala', pos)
                self.match.map.pop(pos)
                eliminated += 1
            pos += 1
        print('Eliminadas', eliminated, 'salas')
