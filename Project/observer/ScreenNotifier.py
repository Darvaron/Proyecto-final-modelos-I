# Descripción: Notifica a la pantalla para que actualice la habilidad
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.Notes import Notes
from .Observer import Observer
import pygame

class ScreenNotifier(Observer):

    def update(self, power):
        Notes.setNote(power)
