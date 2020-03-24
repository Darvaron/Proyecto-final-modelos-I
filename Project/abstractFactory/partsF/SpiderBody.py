# Descripción: Cuerpo concreto de Spider
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.abstractFactory.partsF.Body import Body

class SpiderBody(Body):

    def __init__(self):
        super(SpiderBody, self).__init__('Spider', 'Mordisco', 2000, 50, 3)
