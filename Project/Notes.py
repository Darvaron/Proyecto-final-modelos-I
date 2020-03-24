# Descripción: Se encarga de almacenar un mensaje
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

class Notes():

    Note = None

    @staticmethod
    def setNote(note):
        Notes.Note = note

    @staticmethod
    def getNote():
        return Notes.Note
