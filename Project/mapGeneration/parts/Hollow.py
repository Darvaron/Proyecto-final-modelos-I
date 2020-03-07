# Descripción: Agujeros del mapa
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
import Project.Main


class Hollow:

    def __init__(self):
        self.corners = []
        self.generate_corners()

    def generate_value(self, last, display):  # Genera un nuevo valor de x o y
        n = round(display / 20)
        value = last
        dir = bool(
            random.getrandbits(1))  # Positivo para valores que suman y negativo para los que restan
        while value == last or value > display or value < 0:
            if dir:
                value = last + random.randint(20, n)
            else:
                value = last - random.randint(20, n)
        return value

    def generate_corners(self):
        quantity = random.randint(3, 26)
        posxLastC = 0  # Posiciones de la ultima esquina
        posyLastC = 0
        for n in range(quantity):  # Par coordenado en el origen del agujero
            posxNewC = self.generate_value(posxLastC, Project.Main.displayWidth)
            posyNewC = self.generate_value(posyLastC, Project.Main.displayHeight)
            self.corners.append((posxNewC, posyNewC))
            posxLastC = posxNewC
            posyLastC = posyNewC
