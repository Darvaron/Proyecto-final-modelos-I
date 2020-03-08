# Descripción: Puertas
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
import Project.Main

class Door:

    def __init__(self):
        self.pos = 0
        self.lane = 0  # Número de 1 a 4 representado si esta a la izquierda, arriba, abajo o derecha
        self.generate_door()

    def generate_door(self): #Falta generar logica para unir salas
        lane = random.choice([1, 2, 3, 4])
        if lane == 1 or lane == 4:
            self.pos == random.randint(0, Project.Main.displayHeight)
        else:
            self.pos == random.randint(0, Project.Main.displayWidth)
