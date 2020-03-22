# Descripción: Interfaz del handler
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC, abstractmethod

class MusicHandler(ABC):

    def __init__(self):
        self.succ = None

    @abstractmethod
    def handlerRequest(self,type):
        pass

    def setSucc(self, succ):
        self.succ = succ

    def getSucc(self):
       return self.succ
