# Descripción: Maneja los observadores
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC, abstractmethod

class Subject:

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def dettach(self, observer):
        pass

    @abstractmethod
    def notifyAll(self):
        pass