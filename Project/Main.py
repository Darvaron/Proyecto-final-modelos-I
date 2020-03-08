# Descripción: Main
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import Project.Match

displayWidth = 1366
displayHeight = 768
display = pygame.display.set_mode((displayWidth, displayHeight))
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brightGreen = (0, 200, 0)
brightRed = (200, 0, 0)


def button(message, x, y, w, h, ico, aco, act=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # Ilusión de botón presionado
        pygame.draw.rect(display, ico, (x, y, w, h))
        if click[0] == 1 and act != None:
            act()  # Ejecuta la función
    else:
        pygame.draw.rect(display, aco, (x, y, w, h))
    message_display(message, 'freesansbold.ttf', 20, (x + (w / 2)), (y + (h / 2)))


# Renderiza la superficie para el texto
def text_objects(text, font):
    TextSurface = font.render(text, True, black)  # True del Anti-aliasing
    return TextSurface, TextSurface.get_rect()


# Despliega el mensaje
def message_display(text, font, size, posx, posy):
    largeText = pygame.font.Font(font, size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (posx, posy)
    display.blit(TextSurf, TextRect)


def quit_game():
    pygame.quit()
    quit()


def new_game():
    match = Project.Match.Match()


def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        display.fill(white)
        message_display('Menu', 'freesansbold.ttf', 115, displayWidth / 2, displayHeight / 2)
        button('Empezar', 400, 500, 100, 50, green, brightGreen,
               new_game)  # Falta configurar para que solo se pueda presionar una vez
        button('Salir', 850, 500, 100, 50, red, brightRed, quit_game)
        pygame.display.update()
        clock.tick(10)


def main():
    pygame.init()
    pygame.display.set_caption('The game')
    intro()


if __name__ == "__main__":
    main()
