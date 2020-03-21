# Descripción: Clase decorada de espada,  duplica la distancia distancia de ataque
# Autor: David Armando Rodríguez Varón

from .Decorator import Decorator
import pygame
from shapely.geometry import Polygon

class SwordUpdate(Decorator):

    def __init__(self, player):
        super(SwordUpdate, self).__init__(player)

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

    def getdamageV(self):
        return self._entity.getdamageV()

    def walk(self, case, displayWidth, displayHeight, obstacles, coords):
        self._entity.walk(case, displayWidth, displayHeight, obstacles, coords)

    def attack(self, enemies, coords, coords2):
        playerRec = Polygon(coords2)
        for e in enemies:
            if e.room == self._entity.getRoom():
                coords = [
                    [e.posx, e.posy], [e.posx, e.posy + (e.imageHeight*2)], [e.posx + (e.imageWidth*2), e.posy + (e.imageHeight*2)],
                    [e.posx, e.posy + (e.imageHeight*2)]
                ]
                polygonE = Polygon(coords)
                if polygonE.intersects(playerRec):
                    e.body.defaultLife -= self._entity.getdamageV()
        return enemies

    def die(self, hollows, displayWidth, displayHeight):  # Da una vida extra, da vida infinitas toca arreglar
        return self._entity.die(hollows, displayWidth, displayHeight)

    def standby(self):
        self._entity.standby()

    def setValues(self, choice):
        self._entity.sprite.setValues(choice)

    def draw(self, surface):
        self._entity.sprite.draw(surface, self._entity.getposx(), self._entity.getposy())
        image = pygame.image.load('./resources/powerups/Item__0.png')
        size = image.get_rect().size
        imageWidth = size[0]
        imageHeight = size[1]
        image = pygame.transform.scale(image, ((imageWidth * 2), (imageHeight * 2)))
        surface.blit(image, (self._entity.getposx() + (self._entity.getImageWidth() / 3) - 20, self._entity.getposy()))