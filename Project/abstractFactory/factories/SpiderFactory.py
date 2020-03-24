# Descripción: Fabrica de minotauros
# Autores: David Armando Rodríguez Varón

from Project.abstractFactory.factories.Factory import Factory
from Project.abstractFactory.partsF.SpiderBody import SpiderBody
from Project.abstractFactory.partsF.SpiderSprite import SpiderSprite


class SpiderFactory(Factory):
    def createBody(self):
        return SpiderBody()

    def createSprite(self):
        return SpiderSprite()
