# Descripción: Puertas
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
import pygame


class Door:
    quantity = 0  # Variable estatica que cuenta el número de puertas

    def __init__(self, lane, room, displayWidth, displayHeight):
        self.posx = 0
        self.posy = 0
        self.lane = 0  # Número de 1 a 4 representado si esta a la izquierda, derecha, arriba o abajo
        self.id = 0  # Identificador único de cada puerta
        self.connection = 0  # Identificador de la puerta con la que conecta
        self.image = None
        self.room = room
        self.connected = False
        self.imageWidth = 60
        self.imageHeight = 60
        self.generate_door(lane, displayWidth, displayHeight)

    def set_connection(self, connection):
        self.connection = connection

    def generate_door(self, lane, displayWidth, displayHeight):  # Falta generar logica para unir salas
        self.lane = lane
        self.image = pygame.image.load('./resources/door/door_0.png')
        size = self.image.get_rect().size
        self.imageWidth = size[0]
        self.imageHeight = size[1]
        self.image = pygame.transform.scale(self.image, (self.imageWidth * 2, self.imageHeight * 2))
        size = self.image.get_rect().size
        self.imageWidth = size[0]
        self.imageHeight = size[1]
        if self.lane == 1 or self.lane == 2:
            if self.lane == 1:
                self.posx = 0
            else:
                self.posx = displayWidth - 64
            self.posy = random.randint(0, displayHeight - self.imageHeight)
        else:
            if self.lane == 3:
                self.posy = 0
            else:
                self.posy = displayHeight - 64
            self.posx = random.randint(0, displayWidth - self.imageWidth)
        Door.quantity += 1
        self.id = Door.quantity
        print('Puerta generada en posición x :', self.posx, ', posición y:', self.posy, ', Identificador:', self.id, 'En sala',
              self.room)
