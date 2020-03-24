# Descripción: Clase abstracta de observadores
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC, abstractmethod
import pygame

class Observer:

    @abstractmethod
    def update(self, screen, power):
        pass
