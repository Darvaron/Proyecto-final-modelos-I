# Descripción: Clase concreta command
# Autores: David Armando Rodríguez Varón

from .Command import Command

class CreateParts(Command):

    def __init__(self, fac):
        self.fac = fac

    def execute(self):
        body = self.fac.createBody()
        sprite = self.fac.createSprite()
        return body, sprite