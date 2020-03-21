# Descripción: Fabrica de slimes
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.abstractFactory.factories.Factory import Factory
from Project.abstractFactory.partsF.SlimeBody import SlimeBody
from Project.abstractFactory.partsF.SlimeSprite import SlimeSprite


class SlimeFactory(Factory):

    def createBody(self):
        return SlimeBody()

    def createSprite(self):
        return SlimeSprite()
