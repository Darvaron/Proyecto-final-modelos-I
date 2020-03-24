# Descripción: Clase invocadora
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

class Invoker():

    def __init__(self, command):
        self.command = command

    def run(self):
        return self.command.execute()