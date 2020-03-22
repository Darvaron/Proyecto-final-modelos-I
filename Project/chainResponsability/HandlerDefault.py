# Descripción: Handler especifico por Defecto
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from Project.chainResponsability.MusicHandler import MusicHandler


class HandlerDefault(MusicHandler):

    def handlerRequest(self, type):
        print("No se puede reproducir")