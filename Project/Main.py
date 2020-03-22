# Descripción: Main
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import pygame.gfxdraw
import time
from Project.Game import Game
from Project.chainResponsability.MusicHandler import MusicHandler
from Project.chainResponsability.HandlerHouse import HandlerHouse
from Project.chainResponsability.HandlerMetal import HandlerMetal
from Project.chainResponsability.HandlerRetro import HandlerRetro
from Project.chainResponsability.HandlerDefault import HandlerDefault
from Project.Buttons import *

##1366
##768

# Constants
width = 1366
height = 768

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brightGreen = (0, 200, 0)
brightRed = (200, 0, 0)

# Creating some stuff
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("MENU PRUEBA")
clock = pygame.time.Clock()
music = None

pause = False


# Renderiza la superficie para el texto
def text_objects(text, font):
    TextSurface = font.render(text, True, black)  # True del Anti-aliasing
    return TextSurface, TextSurface.get_rect()


def button(message, x, y, w, h, ico, aco, act=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # Ilusión de botón presionado
        pygame.draw.rect(screen, ico, (x, y, w, h))
        if click[0] == 1 and act != None:
            act()  # Ejecuta la función
    else:
        pygame.draw.rect(screen, aco, (x, y, w, h))
    message_display(message, 'freesansbold.ttf', 20, (x + (w / 2)), (y + (h / 2)))


# Despliega el mensaje
def message_display(text, font, size, posx, posy):
    largeText = pygame.font.Font(font, size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (posx, posy)
    screen.blit(TextSurf, TextRect)


def quit_game():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def resol1():
    width = 1366
    height = 768
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def resol2():
    width = 1920
    height = 1080
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def setting():
    global music
    settingExit = False

    while not settingExit:  # Making a loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit
                quit_game()
            if event.type == pygame.VIDEORESIZE:
                global screen, width, height
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                width, height = event.size
                if width < 600:
                    width = 600
                if height < 400:
                    height = 400
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        screen.fill(white)

        message_display('Resolución', 'freesansbold.ttf', 50, width / 2, height / 2 - 300)
        # Generate Button
        button('1366 x 768', width / 2 - 200, height / 2 - 250, 150, 50, green, brightGreen, resol1)
        button('1920 x 1080', width / 2 + 50, height / 2 - 250, 150, 50, green, brightGreen, resol2)
        message_display('Música', 'freesansbold.ttf', 50, width / 2, height / 2 - 100)
        # Botones musica
        button('House', width / 2 - 70, height / 2 - 50, 150, 50, green, brightGreen, house)
        button('Retro', width / 2 - 270, height / 2 - 50, 150, 50, green, brightGreen, retro)
        button('Metal', width / 2 + 130, height / 2 - 50, 150, 50, green, brightGreen, metal)
        #Boton aceptar
        button('Aceptar', width / 2 - 70, height / 2 + 300, 150, 50, green, brightGreen, new_game)
        message_display('Controles', 'freesansbold.ttf', 50, width / 2, height / 2 + 100)
        message_display('W,A,S,D Para moverte', 'freesansbold.ttf', 50, width / 2, height / 2 + 150)
        message_display('Click Derecho Para atacar', 'freesansbold.ttf', 50, width / 2, height / 2 + 200)
        pygame.display.update()  # Updates only the parameter, if don't it updates all
        clock.tick(144)  # Frames per second


# Tipos de musica

def retro():
    global music
    music = 'retro'


def house():
    global music
    music = 'house'


def metal():
    global music
    music = 'metal'


def pausef():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    unpause()
        screen.fill(white)
        message_display('Pausa', 'freesansbold.ttf', 115, width / 2, height / 2)
        button('Continuar', 400, 500, 100, 50, green, brightGreen,
               unpause)
        button('Salir', 850, 500, 100, 50, red, brightRed, quit_game)
        pygame.display.update()
        clock.tick(10)


def new_game():
    global pause
    gameExit = False
    game = Game(screen, width, height)
    #Aplication Chain of Responsability
    handlers = [HandlerRetro(), HandlerMetal(), HandlerHouse(), HandlerDefault()]
    for m in range(len(handlers)-1):
        handlers[m].setSucc(handlers[m + 1])
    handlers[0].handlerRequest(music)
    print(handlers[0].handlerRequest(music))
    while not gameExit:
        # Input
        typped = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            pause = True
            pausef()
        if key[pygame.K_a]:
            typped.append(1)
        if key[pygame.K_d]:
            typped.append(2)
        if key[pygame.K_w]:
            typped.append(3)
        if key[pygame.K_s]:
            typped.append(4)
        click = pygame.mouse.get_pressed()
        attack = False
        if click[0] == 1:
            typped.append(5)
            attack = True
        game.updateMatch(attack, typped)
        game.displayMatch()
        message_display('Vida: ' + str(game.match.player.getlife()), 'freesansbold.ttf', 30, 90, 50)
        message_display('Stamina: ' + str(game.match.player.getstamina()), 'freesansbold.ttf', 30, 110, 110)
        pygame.display.update()
        clock.tick(13)
        gameExit = game.getGameExit()


def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.VIDEORESIZE:
                global screen, width, height
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                width, height = event.size
                if width < 600:
                    width = 600
                if height < 400:
                    height = 400
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        screen.fill(white)
        message_display('Menu', 'freesansbold.ttf', 115, int(screen.get_width() / 2),
                        int((screen.get_height() / 2) - 100))

        # Load Button Images
        play1 = pygame.image.load("resources/buttons/jugarIna.png")
        play2 = pygame.image.load("resources/buttons/jugarAct.png")

        settings1 = pygame.image.load("resources/buttons/opcIna.png")
        settings2 = pygame.image.load("resources/buttons/opcAct.png")

        exit1 = pygame.image.load("resources/buttons/salirIna.png")
        exit2 = pygame.image.load("resources/buttons/salirAct.png")

        # Generate Button
        playButton = Buttons(play1, play2, round((screen.get_width() / 2) - 100), round((screen.get_height() / 2)) - 50,
                             screen, new_game)
        playButton.update()

        setButton = Buttons(settings1, settings2, round((screen.get_width() / 2) - 100),
                            round((screen.get_height() / 2)) + 30, screen, setting)
        setButton.update()

        exitButton = Buttons(exit1, exit2, round((screen.get_width() / 2) - 100),
                             round((screen.get_height() / 2)) + 110, screen, quit_game)
        exitButton.update()

        pygame.display.update()
        clock.tick(15)


def main():
    pygame.init()
    pygame.display.set_caption('The game')
    intro()


if __name__ == "__main__":
    main()
