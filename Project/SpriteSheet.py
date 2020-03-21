# Descripción: Clase que carga los sprites
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame


class SpriteSheet:

    def __init__(self, file, cols, rows):
        self.sheet = pygame.image.load(file).convert_alpha()
        self.sheetS = self.sheet.get_rect().size
        self.sheet = pygame.transform.scale(self.sheet, (self.sheetS[0]*2 ,self.sheetS[1]*2))
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        self.w = w
        h = self.cellHeight = self.rect.height / rows
        self.h = h
        hw, hh = self.cellCenter = (w / 2, h / 2)

        self.cells = list([(index % cols * w, index // cols * h, w , h) for index in range(self.totalCellCount)])
        self.handle = list([[0, 0], [-hw, 0], [-w, 0], [0, -hh], [-hw, -hh], [-w, -hh], [0, -h], [-hw, -h], [-w, -h]],)

    def draw(self, surface, cellIndex, x, y, handler=4):
        surface.blit(self.sheet, (x + self.handle[handler][0], y + self.handle[handler][1]), self.cells[cellIndex])
