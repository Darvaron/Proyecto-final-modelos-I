# Descripción: Handler especifico para Metal
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.chainResponsability.MusicHandler import MusicHandler
import pygame


class HandlerMetal(MusicHandler):

    def handlerRequest(self, type):
        if type == 'metal':
            pygame.mixer.music.load("./resources/music/metal.wav")
            pygame.mixer.music.play(-1)  # -1 is infinite loop
        else:
            self.succ.handlerRequest(type)