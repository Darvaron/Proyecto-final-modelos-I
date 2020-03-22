# Descripción: composite de puertas
# Autor: David Armando Rodríguez Varón

from Project.mapGeneration.parts.Door import Door

class Composite(Door):

     def __init__(self):
         self.doors = []

     def addPart(self, door):
         self.doors.append(door)

     def verify(self, coords, room):
         intersects = False
         roomV = room
         connec = None
         for d in self.doors:
             if d.room == room:
                if d.verify(coords):
                    connec = d.connection
                    intersects = True
         for d in self.doors:
             if d.id == connec and intersects:
                 roomV = d.room
         return intersects, roomV

     def draw(self, surface, room):
         for d in self.doors:
             if d.room == room:
                 surface.blit(d.image, (d.posx, d.posy))

