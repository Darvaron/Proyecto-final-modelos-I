# Descripción: Handler especifico para Retro
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.chainResponsability.MusicHandler import MusicHandler
import pygame


class HandlerRetro(MusicHandler):

    def handlerRequest(self, type):
        if type == 'retro':
            pygame.mixer.music.load("./resources/music/tetris.wav")
            pygame.mixer.music.play(-1)  # -1 is infinite loop
        else:
            self.succ.handlerRequest(type)