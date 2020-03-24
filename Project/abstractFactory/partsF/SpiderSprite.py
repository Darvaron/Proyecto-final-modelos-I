# Descripción: Clase de sprite de araña
# Autor: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.abstractFactory.partsF.Sprite import Sprite


class SpiderSprite(Sprite):

    def __init__(self):
        super(SpiderSprite, self).__init__(18, 26, 18, 26, 18, 26, 18, 26, 18, 26, 9, 14, 63, 68,
                                           './resources/enemies/spider/Spider.png', 9, 16, 0)
