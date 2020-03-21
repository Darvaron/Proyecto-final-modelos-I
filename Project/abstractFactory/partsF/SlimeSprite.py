# Descripción: Cuerpo concreto de slime
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.abstractFactory.partsF.Sprite import Sprite

class SlimeSprite(Sprite):

    def __init__(self):
        super(SlimeSprite, self).__init__(0, 7, 0, 7, 0, 7, 0, 7, 8, 15, 16, 20, 0, 7, './resources/enemies/slime/slime-Sheet.png', 8, 3, 0)