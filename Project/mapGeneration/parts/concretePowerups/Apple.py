# Descripcipon: Powerup Sombrero
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
import pygame
from Project.mapGeneration.parts.PowerUp import PowerUp


class Apple(PowerUp):

    def __init__(self, hollows, displayWidth, displayHeight):
        super(Apple, self).__init__()
        self.generate_power_up(hollows, displayWidth, displayHeight)

    def generate_power_up(self, hollows, displayWidth, displayHeight):
        self.posx = random.randint(0, displayWidth - self.imageWidth)
        self.posy = random.randint(0, displayHeight - self.imageHeight)
        self.power = 'apple'
        self.image = pygame.image.load('./resources/powerups/Item__4.png')
        size = self.image.get_rect().size
        self.imageWidth = size[0]
        self.imageHeight = size[1]
        self.image = pygame.transform.scale(self.image, ((self.imageWidth * 3), (self.imageHeight * 3)))
        print('PowerUp:', self.power)
        validated = self.validate(hollows, self.posx, self.posy)
        if not validated:
            self.generate_power_up(hollows, displayWidth, displayHeight)
