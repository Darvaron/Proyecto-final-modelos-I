# Descripción: Cuerpo concreto de slime
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.abstractFactory.partsF.Body import Body

class SlimeBody(Body):

    def __init__(self):
        super(SlimeBody, self).__init__('Slime', 'Mordisco', 1500, 20, 2)
