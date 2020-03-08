import pygame

# OTRAS CLASES
from menu.Buttons import *

# Constants
width = 1000
height = 500

# Colors RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
block_color = (53, 115, 255)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Creating some stuff
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("MENU PRUEBA")
clock = pygame.time.Clock()



def text_objects(text, font):
    TextSurface = font.render(text, True, black)  # Anti-aliasing is the True value
    return TextSurface, TextSurface.get_rect()


def button(message, x, y, w, h, ico, aco, act=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # Efecto HOVER
        pygame.draw.rect(screen, ico, (x, y, w, h))
        if click[0] == 1 and act != None:
            act()
    else:
        pygame.draw.rect(screen, aco, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(message, smallText)
    textRect.center = (round(x + (w / 2)), round(y + (h / 2)))
    screen.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def setting():
    settingExit = False

    while not settingExit:  # Making a loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit
                quitgame()

        screen.fill(white)

        pygame.display.update()  # Updates only the parameter, if don't it updates all
        clock.tick(144)  # Frames per second


def game_loop():
    gameExit = False

    while not gameExit:  # Making a loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit
                quitgame()

        screen.fill(white)
        pygame.display.update()  # Updates only the parameter, if don't it updates all
        clock.tick(144)  # Frames per second


def gameintro():
    introGame = True
    while introGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.VIDEORESIZE:
                global screen,width, height
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                width, height = event.size
                if width < 600:
                    width = 600
                if height < 400:
                    height = 400
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                
        screen.fill(white)

        # Fonts
        largeText = pygame.font.Font('freesansbold.ttf', 70)

        # Text
        TextSurf, TextRect = text_objects('Test game', largeText)
        TextRect.center = (int(screen.get_width() / 2), int((screen.get_height() / 2) - 100))

        # Text on Screen
        screen.blit(TextSurf, TextRect)

        # Load Button Images
        play1 = pygame.image.load("resources/jugarIna.png")
        play2 = pygame.image.load("resources/jugarAct.png")

        settings1 = pygame.image.load("resources/opcIna.png")
        settings2 = pygame.image.load("resources/opcAct.png")

        exit1 = pygame.image.load("resources/salirIna.png")
        exit2 = pygame.image.load("resources/salirAct.png")

        # Generate Button
        playButton = Buttons(play1, play2, round((screen.get_width() / 2) - 100), round((screen.get_height() / 2)) - 50, screen, game_loop)
        playButton.update()

        setButton = Buttons(settings1, settings2, round((screen.get_width() / 2) - 100), round((screen.get_height() / 2)) + 30, screen, setting)
        setButton.update()

        exitButton = Buttons(exit1, exit2, round((screen.get_width() / 2) - 100), round((screen.get_height() / 2)) + 110, screen, quitgame)
        exitButton.update()

        # button('Opciones', round((width / 2) - 50), round((height / 2) + 60), 100, 50, green, bright_green)
        # button('Salir', round((width / 2) - 50), round((height / 2) + 120), 100, 50, green, bright_green)

        # Update Screen
        pygame.display.update()
        clock.tick(15)


def main():
    pygame.init()
    gameintro()


if __name__ == "__main__":
    main()
