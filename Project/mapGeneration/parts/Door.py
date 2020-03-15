# Descripción: Puertas
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
import Project.Main


class Door:
    quantity = 0  # Variable estatica que cuenta el número de puertas

    def __init__(self, lane, room):
        self.pos = 0
        self.lane = 0  # Número de 1 a 4 representado si esta a la izquierda, derecha, arriba o abajo
        self.id = 0  # Identificador único de cada puerta
        self.connection = 0  # Identificador de la puerta con la que conecta
        self.imageUrl = None
        self.room = room
        self.connected = False
        self.imageWidth = 60
        self.imageHeight = 60
        self.generate_door(lane)

    '''@staticmethod
    def connect_doors(doors): # Retorna la lista de las puertas a conectar y ser conectadas
        listDoors = doors
        listConn = []
        for n in range(round(Door.quantity/2)):
            doorN = random.randint(0, len(listDoors)-1)
            door = listDoors.pop(doorN)
            listConn.append(door)
        return listDoors, listConn'''

    def set_connection(self, connection):
        self.connection = connection

    def generate_door(self, lane):  # Falta generar logica para unir salas
        self.lane = lane
        if self.lane == 1 or self.lane == 2:
            self.pos = random.randint(0, Project.Main.displayHeight - self.imageHeight)
        else:
            self.pos = random.randint(0, Project.Main.displayWidth - self.imageWidth)
        Door.quantity += 1
        self.id = Door.quantity
        print('Puerta generada en linea:', self.lane, ', posición:', self.pos, ', Identificador:', self.id, 'En sala',
              self.room)
