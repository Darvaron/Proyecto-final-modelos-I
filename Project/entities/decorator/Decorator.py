# Descripción: Clase padre de los decoradores
# Autor: David Armando Rodríguez Varón

from .Entity import Entity


class Decorator(Entity):

    def __init__(self, entity):
        self._entity = entity
