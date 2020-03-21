# Descripción: Enemigos
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Enemy():

    def __init__(self, body, sprite, hollows, displayWidth, displayHeight, room, collision=True):
        self.body = body
        self.sprite = sprite
        self.posx = 0
        self.posy = 0
        self.collision = collision
        self.room = room
        self.imageWidth = self.sprite.sprites.w
        self.imageHeight = self.sprite.sprites.h
        self.setPos(hollows, displayWidth, displayHeight)

    def setPos(self, hollows, displayWidth, displayHeight):
        self.posx = random.randint(0, displayWidth - self.imageWidth)
        self.posy = random.randint(0, displayHeight - self.imageHeight)
        pos = Point(self.posx, self.posy)
        validated = True
        for h in hollows:
            polygon = Polygon(h.corners)
            if polygon.contains(pos):
                validated = False
        if not validated:
            self.setPos(hollows, displayWidth, displayHeight)
        print('Enemigo :', self.body.getName(), 'generado en la sala:', self.room)

    def setValues(self, choice):
        self.sprite.setValues(choice)

    def draw(self, surface):
        self.sprite.draw(surface, self.posx, self.posy)

    def verifyPos(self, copyx, copyy, hollows):

        '''randomLoc = random.randint(0, 10) #Falta generar algoritmo que esquive agujeros
        randomChoice = random.randint(0, 4)
        if randomChoice == 1:
            self.posx += randomLoc
            self.posy += randomLoc
        elif randomChoice == 2:
            self.posx += randomLoc
            self.posy -= randomLoc
        elif randomChoice == 3:
            self.posx -= randomLoc
            self.posy += randomLoc
        else:
            self.posx -= randomLoc
            self.posy -= randomLoc
        self.verifyPos(copyx, copyx, hollows)'''

        valid = True
        for h in hollows:
            poly = Polygon(h.corners)
            pos = Point(self.posx, self.posy)
            if poly.contains(pos):
                self.posx = copyx
                self.posy = copyy
                valid = False
        return valid

    def track(self, posx, posy, hollows, obstacles):
        valid = True
        copyx = self.posx
        copyy = self.posy
        if self.posx > posx:
            self.posx -= self.body.speed
        else:
            self.posx += self.body.speed
        if self.posy > posy:
            self.posy -= self.body.speed
        else:
            self.posy += self.body.speed
        coords = [
            [self.posx, self.posy], [self.posx, self.posy + self.imageHeight],
            [self.posx + self.imageWidth, self.posy + self.imageHeight],
            [self.posx, self.posy + self.imageHeight]
        ]
        enemyRec = Polygon(coords)
        for o in obstacles:
            coordsObs = [
                [o.posx, o.posy], [o.posx + (o.imageWidth / 3), o.posy],
                [o.posx + (o.imageWidth / 3), o.posy + (o.imageHeight / 3)],
                [o.posx, (o.posy + o.imageHeight / 3)]
            ]
            polygonO = Polygon(coordsObs)
            if enemyRec.intersects(polygonO):
                valid = False
        if valid:
            valid = self.verifyPos(copyx, copyy, hollows)
        if not valid:
            self.posx -= self.posx - copyx - 2
            self.posy -= self.posy - copyy - 2
        # self.verifyPos(copyx, copyy,hollows)

    def attack(self, coords2, room, life):
        playerRecFeets = Polygon(coords2)
        if self.room == room:
            coords = [
                [self.posx, self.posy], [self.posx, self.posy + self.imageHeight],
                [self.posx + self.imageWidth, self.posy + self.imageHeight],
                [self.posx, self.posy + self.imageHeight]
            ]
            polygonE = Polygon(coords)
            if polygonE.intersects(playerRecFeets):
                life -= self.body.damage
        return life
