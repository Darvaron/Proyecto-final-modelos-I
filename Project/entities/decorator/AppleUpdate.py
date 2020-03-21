# Descripción: Clase decorada apple, da velocidad
# Autor: David Armando Rodríguez Varón

from .Decorator import Decorator
import pygame
from shapely.geometry import Polygon


class AppleUpdate(Decorator):

    def __init__(self, player):
        super(AppleUpdate, self).__init__(player)

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
        playerRec = Polygon(coords)
        posx = self._entity.getposx()
        posy = self._entity.getposy()
        if case == 1:  # izquierda
            self._entity.setposx(self._entity.getposx() - 2 * self._entity.getSpeed())
        elif case == 2:  # Derecha
            self._entity.setposx(self._entity.getposx() + 2 * self._entity.getSpeed())
        elif case == 3:  # Arriba
            self._entity.setposy(self._entity.getposy() - 2 * self._entity.getSpeed())
        else:  # Abajo
            self._entity.setposy(self._entity.getposy() + 2 * self._entity.getSpeed())
        valid = True
        for o in obstacles:
            coordsObs = [
                [o.posx, o.posy], [o.posx + (o.imageWidth / 3), o.posy],
                [o.posx + (o.imageWidth / 3), o.posy + (o.imageHeight / 3)],
                [o.posx, (o.posy + o.imageHeight / 3)]
            ]
            polygonO = Polygon(coordsObs)
            if playerRec.intersects(polygonO):
                valid = False
        if self._entity.getposy() < 0 or self._entity.getposy() > displayHeight:
            self._entity.setposy(posy)
        if self._entity.getposx() < 0 or self._entity.getposx() > displayWidth:
            self._entity.setposx(posx)
        if not valid:
            self._entity.setposx(self._entity.getposx() - (self._entity.getposx() - posx - 2))
            self._entity.setposy(self._entity.getposy() - (self._entity.getposy() - posy - 2))

    def attack(self, enemies, coords, coords2):
        return self._entity.attack(enemies, coords, coords2)

    def die(self, hollows, displayWidth, displayHeight):  # Da una vida extra, da vida infinitas toca arreglar
        return self._entity.die(hollows, displayWidth, displayHeight)

    def standby(self):
        self._entity.standby()

    def setValues(self, choice):
        self._entity.sprite.setValues(choice)

    def draw(self, surface):
        self._entity.sprite.draw(surface, self._entity.getposx(), self._entity.getposy())
        image = pygame.image.load('./resources/powerups/Item__4.png')
        size = image.get_rect().size
        imageWidth = size[0]
        imageHeight = size[1]
        image = pygame.transform.scale(image, ((imageWidth * 2), (imageHeight * 2)))
        surface.blit(image, (self._entity.getposx() - (self._entity.getImageWidth() / 3) + 20, self._entity.getposy()))
