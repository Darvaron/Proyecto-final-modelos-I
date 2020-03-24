# Descripción: Clase command patron command
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass