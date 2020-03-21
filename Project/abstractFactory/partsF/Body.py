# Descripción: Cuerpo de los enemigos
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

from abc import ABC


class Body(ABC):

    def __init__(self):
        self.name = ''
        self.skillName = ''
        self.defaultLife = 0
        self.damage = 0

    def __init__(self, name, skillName, defaultLife, damage, speed):
        self.name = name
        self.skillName = skillName
        self.defaultLife = defaultLife
        self.damage = damage
        self.speed = speed

    def getName(self):
        return self.name

    def getSkillName(self):
        return self.skillName

    def getDefaultLife(self):
        return self.defaultLife