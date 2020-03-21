# Descripción: Personaje
# Autor: David Armando Rodríguez Varón


from .Entity import Entity
from shapely.geometry.polygon import Polygon


class Player(Entity):

    def __init__(self, hollows, displayWidth, displayHeight, room, actRoom):
        super(Player, self).__init__(0, 0, room, actRoom, hollows, displayWidth, displayHeight)


    def walk(self, case, displayWidth, displayHeight, obstacles, coords):
        playerRec = Polygon(coords)
        posx = self.posx
        posy = self.posy
        if case == 1:  # izquierda
            self.posx -= self.speed
        elif case == 2:  # Derecha
            self.posx += self.speed
        elif case == 3:  # Arriba
            self.posy -= self.speed
        else:  # Abajo
            self.posy += self.speed
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
        if self.posy < 0 or self.posy > displayHeight:
            self.posy = posy
        if self.posx < 0 or self.posx > displayWidth:
            self.posx = posx
        if not valid:
            self.posx -= self.posx - posx - 2
            self.posy -= self.posy - posy - 2

    def attack(self, enemies, coords, coords2):
        playerRec = Polygon(coords2)
        for e in enemies:
            if e.room == self.room:
                coords = [
                    [e.posx, e.posy], [e.posx, e.posy + e.imageHeight], [e.posx + e.imageWidth, e.posy + e.imageHeight],
                    [e.posx, e.posy + e.imageHeight]
                ]
                polygonE = Polygon(coords)
                if polygonE.intersects(playerRec):
                    e.body.defaultLife -= self.damageV
        return enemies

    def die(self, hollows, displayWidth, displayHeight):
        return True

    def standby(self):
        pass