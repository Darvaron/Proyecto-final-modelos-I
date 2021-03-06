# Descripción: Agujeros del mapa
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import random
from shapely.geometry import Polygon


# Falta redondear los agujeros
class Hollow:

    def __init__(self, displayWidth, displayHeight):
        self.corners = []
        self.generate_points(displayWidth, displayHeight)

    def round_out(self, displayWidth, displayHeight):  # Redondea poligono
        polygon = Polygon(self.corners)
        '''Returns an approximate representation of all points within a given distance of the this geometric object.
        A positive distance has an effect of dilation; a negative distance, erosion. The optional resolution argument
        determines the number of segments used to approximate a quarter circle around a point.'''

        polygon = polygon.buffer(600, join_style=1).buffer(-600.0, join_style=1)
        if polygon.__class__ == 'shapely.geometry.multipolygon.MultiPolygon':
            self.generate_points(displayWidth, displayHeight)
        pos = polygon.exterior.coords # Salta error de multipolygon muy de vez en cuando
        self.corners = pos
        if len(self.corners) < 3:  # Si minimo no quedan 3 coordenadas
            self.generate_points(displayWidth, displayHeight)

    def valid(self, displayWidth, displayHeight):
        validV = True
        for coord in self.corners:  # Verifica que no se salga de la ventana
            x = coord[0]
            y = coord[1]
            if x > displayWidth or x < 0:
                validV = False
            if y > displayHeight or y < 0:
                validV = False
        polygonValidator = Polygon(self.corners)
        if polygonValidator.area < 20000 or not polygonValidator.is_valid:  # Verifica que los poligonos no sean muy delgados
            validV = False
        long = len(self.corners) - 1
        for n in range(long):  # Verifica que no hayan puntos muy lejanos entre si
            coord1x = self.corners[n][0]
            coord1y = self.corners[n][1]
            coord2x = self.corners[n + 1][0]
            coord2y = self.corners[n + 1][1]
            if abs(coord1x - coord2x) + abs(coord1y - coord2y) > 70:
                validV: False
        return validV

    def generate_points(self, displayWidth, displayHeight):
        self.corners = []
        quantity = random.randint(5, 8)
        posxOrigin = random.randint(round(displayWidth / 5), round(4 * displayWidth / 5))
        posyOrigin = random.randint(round(displayHeight / 5), round(4 * displayHeight / 5))
        for n in range(quantity):
            direction = random.randint(0, 5)
            if direction == 1:
                posx = posxOrigin + random.randint(round(displayHeight / 15),
                                                   round(displayWidth / 9))
                posy = posyOrigin
            elif direction == 2:
                posx = posxOrigin
                posy = posyOrigin + random.randint(round(displayHeight / 15),
                                                   round(displayHeight / 9))
            elif direction == 3:
                posx = posxOrigin - random.randint(round(displayHeight / 15),
                                                   round(displayWidth / 9))
                posy = posyOrigin

            else:
                posx = posxOrigin
                posy = posyOrigin - random.randint(round(displayHeight / 10),
                                                   round(displayHeight / 9))
            self.corners.append([posx, posy])
            posxOrigin = posx
            posyOrigin = posy
        if not self.valid(displayWidth, displayHeight):
            self.generate_points(displayWidth, displayHeight)
        self.round_out(displayWidth, displayHeight)
