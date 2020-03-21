# Descripción: Clase abstracta de los decoradores y player
# Autor: David Armando Rodríguez Varón

import random
from shapely.geometry import Point, Polygon
from abc import ABC, abstractmethod
from Project.abstractFactory.partsF.Sprite import Sprite


class Entity(ABC):

    def __init__(self, posx, posy, room, actRoom, hollows, displayWidth, displayHeight):
        self.posx = posx;
        self.posy = posy;
        self.sprite = Sprite(20, 25, 14, 19, 9, 13, 4, 8, 35, 37, 0, 3, 0, 3, './resources/character/charSheet.png', 8,
                             5, 0)
        self.life = 2000;
        self.stamina = 1000;
        self.speed = 10;
        self.imageWidth = self.sprite.sprites.w
        self.imageHeight = self.sprite.sprites.h
        self.room = room
        self.actRoom = actRoom
        self.damage = True
        self.damageV = 40
        self.setposition(hollows, displayWidth, displayHeight)

    def setposition(self, hollows, displayWidth, displayHeight):
        self.posx = random.randint(0, displayWidth - self.imageWidth)
        self.posy = random.randint(0, displayHeight - self.imageHeight)
        pos = Point(self.posx, self.posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        if not validated:
            self.setposition(hollows, displayWidth, displayHeight)

    def getdamageV(self):
        return self.damageV

    def getSpeed(self):
        return self.speed

    def setActRoom(self, actRoom):
        self.actRoom  = actRoom

    def getActRoom(self):
        return self.actRoom

    def getLastChoice(self):
        return self.sprite.lastChoice

    def getImageWidth(self):
        return self.imageWidth

    def getImageHeigth(self):
        return self.imageHeight

    def getRoom(self):
        return self.room

    def setposx(self, posx):
        self.posx = posx

    def setposy(self, posy):
        self.posy = posy

    def getposx(self):
        return self.posx

    def getposy(self):
        return self.posy

    def setRoom(self, room):
        self.room = room

    def getlife(self):
        return self.life

    def getstamina(self):
        return self.stamina

    def setlife(self, life):
        self.life = life

    def setstamina(self, stamina):
        self.stamina = stamina

    @abstractmethod
    def walk(self, case, displayWidth, displayHeight, obstacles, coords):
        pass

    @abstractmethod
    def attack(self, enemies, coords, coords2):
        pass

    @abstractmethod
    def die(self, hollows, displayWidth, displayHeight):
        pass

    @abstractmethod
    def standby(self):
        pass

    def setValues(self, choice):
        self.sprite.setValues(choice)

    def draw(self, surface):
        self.sprite.draw(surface, self.posx, self.posy)
