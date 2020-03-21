# Descripción: Creador concreto de partida normal
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from Project.matchGeneration.MatchBuilder import MatchBuilder
from Project.mapGeneration.MapDir import MapDir
from Project.mapGeneration.concreteMapsCreators.defaultMap import defaultMap
from Project.mapGeneration.Map import Map
from Project.mapGeneration.parts.Door import Door
from Project.entities.Enemy import Enemy
from Project.abstractFactory.factories.SlimeFactory import SlimeFactory
from Project.entities.decorator.Player import Player

class NormalMatch(MatchBuilder):  # Construye una partida normal

    def createMaps(self, displayWidth, displayHeight):
        self.match.map = []
        self.match.doors = []
        self.doors = []
        map = []
        Door.quantity = 0
        Map.quantity = 0
        quantity = random.randint(2, 8)
        for n in range(quantity):
            # Mapa generado mediante builder
            mapDirector = MapDir()
            mapDirector.set_map_creator(defaultMap())
            mapDirector.construct(Map.quantity, displayWidth, displayHeight)
            map.append(mapDirector.get_map())
            for d in map[n].doors:
                self.match.doors.append(d)
            Map.quantity += 1
            print('Sala', n, 'generada')
        self.match.setMaps(map)

    def createDoors(self):
        newDoors = []
        for d in self.match.doors:  # Asigna conexiones entre pares de puertas
            for c in self.match.doors:
                if d.room != c.room and not d.connected and not c.connected:
                    d.connected = True
                    c.connected = True
                    c.set_connection(d.id)
                    d.set_connection(c.id)
                    newDoors.append(c)
                    newDoors.append(d)
                    break
        self.match.setDoors(newDoors)
        for n in self.doors:
            print('Puerta ', n.id, 'conectada con:', n.connection)
        print('Conexiones generadas correctamente')
        self.delete_empty(self)

    def createEnemies(self, maps, displayWidth, displayHeight):
        quantity = random.randint(0, 4);
        enemies = []
        mNumber = 0
        for m in maps:
            for e in range(quantity):
                fac = None
                factDecision = random.randint(0, 0)  # Valor a cambiar cuando existan mas fabricas de partes
                if factDecision == 0: #Usamos abstract factory
                    fac = SlimeFactory()
                enemy = Enemy(fac.createBody(), fac.createSprite(), m.hollows, displayWidth, displayHeight, mNumber, True)
                enemies.append(enemy)
            mNumber += 1
        self.match.setEnemies(enemies)
        print('Generados ', len(enemies), 'enemigos')

    def createPlayer(self, maps, displayWidth, displayHeight):
        availableRooms = []
        for m in maps:
            availableRooms.append(m.id)
        room = random.choice(availableRooms)
        map = None
        actRoom = 0
        n = 0
        for m in maps:
            if m.id == room:
                map = m
                actRoom = n
            n += 1
        self.match.setPlayer(Player(map.hollows, displayWidth, displayHeight, room, actRoom))
        print('Personaje generado correctamente en la sala', room)
