# Descripción: Clase concreta de sujeto
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from .Subject import Subject


class PowerObtained(Subject):
    observers = []

    def attach(self, observer):
        PowerObtained.observers.append(observer)

    def dettach(self, observer):
        PowerObtained.observers.remove(observer)

    def notifyAll(self, power):
        for o in PowerObtained.observers:
            o.update(power)
