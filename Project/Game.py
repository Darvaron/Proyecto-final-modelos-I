# Descripción: Clase que se encarga de manejar la partida
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
from Project.matchGeneration.MatchDirector import MatchDirector
from Project.matchGeneration.conreteMatchCreators.NormalMatch import NormalMatch
from shapely.geometry import Polygon, Point
from Project.entities.decorator.HatUpdate import HatUpdate
from Project.entities.decorator.AppleUpdate import AppleUpdate
from Project.entities.decorator.SwordUpdate import SwordUpdate
from Project.composite.Composite import Composite

class Game:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    brightGreen = (0, 200, 0)
    brightRed = (200, 0, 0)

    def __init__(self, surface, displayWidth, displayHeight):
        self.display = surface
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.gameExit = False
        self.match = None
        self.doors = None
        self.create()

    def create(self):  # Crea la partida
        matchDir = MatchDirector()
        normal = NormalMatch()
        matchDir.defBuilder(normal)
        matchDir.construct(self.displayWidth, self.displayHeight)
        self.match = matchDir.getMatch()
        for e in self.match.enemies:  # Setea a los enemigos en modo espera
            e.setValues(7)
        self.match.player.setValues(7)
        #Añade composite
        self.doors = Composite()
        for d in self.match.doors:
            self.doors.addPart(d)

    def updateMatch(self, attack, typped=[]):  # Actualiza la partida
        # self.match.player.damage = True
        # Coordenadas de la hitbox de los pies del personaje
        coords = [[self.match.player.getposx() - (self.match.player.getImageWidth() / 6),
                   self.match.player.getposy() + (self.match.player.getImageHeigth() / 4)],
                  [self.match.player.getposx() + (self.match.player.getImageWidth() / 6),
                   self.match.player.getposy() + (self.match.player.getImageHeigth() / 4)],
                  [self.match.player.getposx() + (self.match.player.getImageWidth() / 6),
                   self.match.player.getposy() + (self.match.player.getImageHeigth() / 2)],
                  [self.match.player.getposx() - (self.match.player.getImageWidth() / 6),
                   self.match.player.getposy() + (self.match.player.getImageHeigth() / 2)]
                  ]
        # Hitbox del personaje completo
        coords2 = [
            [self.match.player.getposx() - self.match.player.getImageWidth() / 4,
             self.match.player.getposy() - self.match.player.getImageWidth() / 2],
            [self.match.player.getposx() + self.match.player.getImageWidth() / 4,
             self.match.player.getposy() - self.match.player.getImageWidth() / 2],
            [self.match.player.getposx() + self.match.player.getImageWidth() / 4,
             self.match.player.getposy() + self.match.player.getImageWidth() / 2],
            [self.match.player.getposx() - self.match.player.getImageWidth() / 4,
             self.match.player.getposy() + self.match.player.getImageWidth() / 2]
        ]
        if attack:
            self.match.setEnemies(self.match.player.attack(self.match.enemies, coords, coords2))
        # Posicion del personaje
        for t in typped:
            if t < 5:
                self.match.player.walk(t,
                                       self.displayWidth,
                                       self.displayHeight,
                                       self.match.maps[
                                           self.match.player.getRoom()].obstacles,
                                       coords)
            if t == 6:
                pass
                # self.match.player.attack(self.match.enemies, coords2)
        n = 0
        for e in self.match.enemies:
            if e.body.defaultLife <= 0:
                self.match.enemies.pop(n)
            else:
                if e.room == self.match.player.getRoom():
                    self.match.player.setlife(
                        e.attack(coords, self.match.player.getRoom(), self.match.player.getlife()))
                    e.track(self.match.player.getposx(), self.match.player.getposy(),
                            self.match.maps[self.match.player.getRoom()].hollows,
                            self.match.maps[self.match.player.getRoom()].obstacles)
                pointE = Point(e.posx, e.posy)
                pointCharacter = Point(self.match.player.getposx(), self.match.player.getposy())
                #Cambia la imagen en relación a la distancia
                if pointE.distance(pointCharacter) < 300 and e.sprite.lastChoice != 5:
                    e.setValues(5)
                elif pointE.distance(pointCharacter) >= 300 and e.sprite.lastChoice != 7:
                    e.setValues(7)
            n += 1
        # Actualiza la imagen jugador
        if len(typped) > 0:
            if self.match.player.getLastChoice() != typped[-1]:
                self.match.player.setValues(typped[-1])
        elif len(typped) == 0:
            if self.match.player.getLastChoice() != 7:
                self.match.player.setValues(7)
        # Verifica que no se caiga a un hueco
        polygonChar = Polygon(coords)
        for h in self.match.maps[self.match.player.getActRoom()].hollows:
            polygon = Polygon(h.corners)
            if (polygonChar.intersects(polygon)):
                print('Cambia estado a terminado, personaje muerto')
                self.gameExit = self.match.player.die(self.match.maps[self.match.player.getActRoom()].hollows,
                                                      self.displayWidth, self.displayHeight)
        # Si no tiene vida
        if self.match.player.getlife() <= 0:
            self.gameExit = self.match.player.die(self.match.maps[self.match.player.getActRoom()].hollows,
                                                  self.displayWidth, self.displayHeight)
        # Verifica si coje algun powerup
        if self.match.maps[self.match.player.getActRoom()].powerUps != None:
            p = self.match.maps[self.match.player.getActRoom()].powerUps
            coordsPower = [
                [p.posx, p.posy], [p.posx + (p.imageWidth * 3), p.posy],
                [p.posx + (p.imageWidth * 3), p.posy + (p.imageHeight * 3)], [p.posx, p.posy + (p.imageHeight * 3)]
            ]
            polygonFeet = Polygon(coords)
            polygonUp = Polygon(coordsPower)
            if polygonUp.intersects(polygonFeet):
                #Decorator
                if p.power == 'hat':
                    self.match.player = HatUpdate(self.match.player)
                elif p.power == 'apple':
                    self.match.player = AppleUpdate(self.match.player)
                elif p.power == 'sword':
                    self.match.player = SwordUpdate(self.match.player)
                self.match.maps[self.match.player.getActRoom()].powerUps = None
        #Puertas (Uso del composite)
        connectsdoor, room = self.doors.verify(coords, self.match.player.getActRoom())
        if connectsdoor:
            self.match.player.setRoom(room)
            self.match.player.setActRoom(room)
            self.match.player.setposition(self.match.maps[self.match.player.getRoom()].hollows, self.displayWidth, self.displayHeight)

    def displayMatch(self):  # Muestra la partida
        displayedx = 0
        displayedy = 0
        text = self.match.maps[self.match.player.getActRoom()].textures[0]
        size = text.get_rect().size
        while displayedx < self.displayWidth:
            displayedy = 0
            while displayedy < self.displayHeight:
                self.display.blit(text, (displayedx, displayedy))
                displayedy += size[1]
            displayedx += size[0]
        # Agujeros
        for h in self.match.maps[self.match.player.getActRoom()].hollows:
            pygame.gfxdraw.aapolygon(self.display, h.corners, Game.black)
            pygame.gfxdraw.filled_polygon(self.display, h.corners, Game.black)
        # Puertas
        self.doors.draw(self.display, self.match.player.getActRoom())
        # Objetos
        for o in self.match.maps[self.match.player.getActRoom()].obstacles:
            self.display.blit(o.image, (o.posx, o.posy))
        # Powerup
        if self.match.maps[self.match.player.getActRoom()].powerUps != None:
            self.display.blit(self.match.maps[self.match.player.getActRoom()].powerUps.image, (
                self.match.maps[self.match.player.getRoom()].powerUps.posx,
                self.match.maps[self.match.player.getRoom()].powerUps.posy))
        # Enemigo
        for e in self.match.enemies:
            if self.match.player.getActRoom() == e.room:
                e.draw(self.display)
                pygame.draw.rect(self.display, Game.green, (
                    e.posx - (e.sprite.sprites.w / 2), e.posy - (e.sprite.sprites.h / 2), e.body.defaultLife / 20, 7))
        # Jugador
        self.match.player.draw(self.display)
        # Vida y stamina
        pygame.draw.rect(self.display, Game.red, (10, 10, self.match.player.getlife() / 10, 20))
        pygame.draw.rect(self.display, Game.blue, (10, 70, self.match.player.getstamina() / 10, 20))

    def getGameExit(self):
        return self.gameExit
