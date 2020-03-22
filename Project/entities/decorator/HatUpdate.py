# Descripción: Clase decorada con sombrero, da una inmortalidad ante los agujeros
# Autor: David Armando Rodríguez Varón

from .Decorator import Decorator
import pygame


class HatUpdate(Decorator):

    def __init__(self, player):
        super(HatUpdate, self).__init__(player)

    def setposition(self, hollows, displayWidth, displayHeight):
        self._entity.setposition(hollows, displayWidth, displayHeight)

    def getdamageV(self):
        return self._entity.getdamageV()

    def setActRoom(self, actRoom):
        self._entity.setActRoom(actRoom)

    def getActRoom(self):
        return self._entity.getActRoom()

    def getLastChoice(self):
        return self._entity.getLastChoice()

    def getImageWidth(self):
        return self._entity.getImageWidth()

    def getImageHeigth(self):
        return self._entity.getImageHeigth()

    def getRoom(self):
        return self._entity.getRoom()

    def getposx(self):
        return self._entity.getposx()

    def getposy(self):
        return self._entity.getposy()

    def setRoom(self, room):
        self._entity.setRoom(room)

    def getlife(self):
        return self._entity.getlife()

    def getstamina(self):
        return self._entity.getstamina()

    def setlife(self, life):
        self._entity.setlife(life)

    def setstamina(self, stamina):
        self._entity.setstamina(stamina)

    def getSpeed(self):
        return self._entity.getSpeed()

    def setposx(self, posx):
        self._entity.setposx(posx)

    def setposy(self, posy):
        self._entity.setposy(posy)

    def walk(self, case, displayWidth, displayHeight, obstacles, coords):
        self._entity.walk(case, displayWidth, displayHeight, obstacles, coords)

    def attack(self, enemies, coords, coords2):
        return self._entity.attack(enemies, coords, coords2)

    def die(self, hollows, displayWidth, displayHeight):  # Da una vida extra, da vida infinitas toca arreglar
        self._entity.setlife(2000)
        self._entity.setposition(hollows, displayWidth, displayHeight)
        return False

    def standby(self):
        self._entity.standby()

    def setValues(self, choice):
        self._entity.setValues(choice)

    def draw(self, surface):
        self._entity.draw(surface)
        image = pygame.image.load('./resources/powerups/Item__3.png')
        size = image.get_rect().size
        imageWidth = size[0]
        imageHeight = size[1]
        image = pygame.transform.scale(image, ((imageWidth * 3), (imageHeight * 3)))
        surface.blit(image, (self._entity.getposx() - (self._entity.getImageWidth() / 5) + 10,
                             self._entity.getposy() - (self._entity.getImageHeigth() / 2) - 25))
