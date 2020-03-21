# Descripción: Sprites del personaje
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.SpriteSheet import SpriteSheet
from abc import ABC


class Sprite(ABC):

    def __init__(self, wkBl, wkFl, wkBr, wkFr, wkBu, wkFu, wkBd, wkFd, AtB, AtF, DB, DF, WB, WF, fileD, col, row, imgAct=0):
        self.defineValues(wkBl, wkFl, wkBr, wkFr, wkBu, wkFu, wkBd, wkFd, AtB, AtF, DB, DF, WB, WF, imgAct=0)
        self.sprites = SpriteSheet(fileD, col, row)

    def defineValues(self, wkBl, wkFl, wkBr, wkFr, wkBu, wkFu, wkBd, wkFd, AtB, AtF, DB, DF, WB, WF, imgAct=0):
        self.wkBl = wkBl #Izquierdas
        self.wkFl = wkFl
        self.wkBr = wkBr #Derecha
        self.wkFr = wkFr
        self.wkBu = wkBu #Arriba
        self.wkFu = wkFu
        self.wkBd = wkBd #Abajo
        self.wkFd = wkFd
        self.AtB = AtB #Atacar
        self.AtF = AtF
        self.DB = DB #Muerte
        self.DF = DF
        self.WB = WB #En espera
        self.WF = WF
        self.imgAct = imgAct
        self.limit = 0
        self.choice = 0
        self.lastChoice = 0

    def draw(self, surface, posx, posy):
        self.sprites.draw(surface, self.imgAct % (self.limit+1), posx, posy)
        if self.imgAct == self.limit:
            self.setValues(self.choice)
        self.imgAct += 1

    def setValues(self, choice):
        self.choice = choice
        self.lastChoice = choice
        if choice == 1: #Izq
            self.imgAct = self.wkBl
            self.limit = self.wkFl

        elif choice == 2: #Derecha
            self.imgAct = self.wkBr
            self.limit = self.wkFr

        elif choice == 3: #Arriba
            self.imgAct = self.wkBu
            self.limit = self.wkFu

        elif choice == 4: #Abajo
            self.imgAct = self.wkBd
            self.limit = self.wkFd

        elif choice == 5: #Atacar
            self.imgAct = self.AtB
            self.limit = self.AtF
        elif choice == 6: #Muere
            self.imgAct = self.DB
            self.limit = self.DF
        else: #ESpera
            self.imgAct =self.WB
            self.limit = self.WF

