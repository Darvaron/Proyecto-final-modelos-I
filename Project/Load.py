# Descripción: Clase partida
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from Project.mapGeneration.MapDir import MapDir
from Project.mapGeneration.concreteMapsCreators.defaultMap import defaultMap
from Project.mapGeneration.parts.Door import Door
from Project.mapGeneration.Map import Map


class Load:

    def __init__(self):
        self.map = []
        self.doors = []  # Puertas de todo el mapa
        self.generate_match()

    def generate_doors(self):  # Genera las puertas conectadas para la partida
        #if Door.quantity % 2 != 0:  # Si no corresponde el número de puertas
        #    self.generate_map()
        #    print('Generación de puertas impares: no valido')
        newDoors = []
        for d in self.doors: #Asigna conexiones entre pares de puertas
            for c in self.doors:
                if d.room != c.room and not d.connected and not c.connected:
                    d.connected = True
                    c.connected = True
                    c.set_connection(d.id)
                    d.set_connection(c.id)
                    newDoors.append(c)
                    newDoors.append(d)
                    break

        '''doorsAvailable, connections = Door.connect_doors(self.doors)  # Lista de pares de id y sala      
        dn = 0 #Contadores
        for d in doorsAvailable:
            cn = 0
            for c in connections:
                if d.room != c.room:  # Asigna conectores
                    newDoor1 = d
                    newDoor2 = c
                    newDoor1.set_connection(c.id)
                    newDoor2.set_connection(d.id)
                    newDoors.append(newDoor1)
                    newDoors.append(newDoor2)
                    #doorsAvailable.pop(dn)
                    connections.pop(cn)
                    break
                cn += 1
            dn += 1'''
        self.doors = newDoors
        for n in self.doors:
            print('Puerta ', n.id, 'conectada con:', n.connection)
        print('Conexiones generadas correctamente')

    def append_doors(self, doors): #Añade las puertas de una sala a las puertas del mapa en general
        for d in doors:
            self.doors.append(d)

    def generate_map(self):
        self.map = []
        self.doors = []
        Door.quantity = 0
        Map.quantity = 0
        quantity = random.randint(2, 8)
        for n in range(quantity):
            # Mapa generado mediante builder
            mapDirector = MapDir()
            mapDirector.set_map_creator(defaultMap())
            mapDirector.construct(Map.quantity)
            self.map.append(mapDirector.get_map())
            self.append_doors(self.map[n].doors)
            Map.quantity += 1
            print('Sala', n, 'generada')

    def delete_empty(self): #Elimina salas sin puertas
        pos = 0
        eliminated = 0
        for m in self.map:
            hasDoors = False
            for d in self.doors:
                if d.room == m.id:
                    hasDoors = True
            if not hasDoors:
                print('Eliminando sala', pos)
                self.map.pop(pos)
                eliminated += 1
            pos += 1
        print('Eliminadas', eliminated, 'salas')


    def generate_match(self):
        self.generate_map()
        self.generate_doors()
        self.delete_empty()
