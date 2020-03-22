# Descripción: Handler especifico para House
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.chainResponsability.MusicHandler import MusicHandler
import pygame


class HandlerHouse(MusicHandler):

    def handlerRequest(self,type):
        if type == 'house':
            pygame.mixer.music.load("./resources/music/house.wav")
            pygame.mixer.music.play(-1)  # -1 is infinite loop
        else:
            self.succ.handlerRequest(type)
