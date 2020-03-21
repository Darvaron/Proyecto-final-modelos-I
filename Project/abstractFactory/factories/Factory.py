# Descripción: Fabrica abstract
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC
from abc import abstractmethod


class Factory(ABC):

    @abstractmethod
    def createBody(self):
        pass

    @abstractmethod
    def createSprite(self):
        pass
