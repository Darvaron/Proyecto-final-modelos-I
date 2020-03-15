# Descripción: Main
# Autores: David Armando Rodríguez Varón, Juan Sebastián Sánchez Tabares

import pygame
import pygame.gfxdraw
import Project.Load
import time

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
    gameExit = False
    while not gameExit:
        load = Project.Load.Load()
        gameExit = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        n = 0
        for m in load.map: #Impresion de muestra de todas las salas
            display.fill(white)
            # Agujeros
            for h in m.hollows:
                pygame.gfxdraw.aapolygon(display, h.corners, black)
                pygame.gfxdraw.filled_polygon(display, h.corners, black)
            # Puertas
            for door in load.doors:
                if door.room == m.id: # Si las puertas estan en la misma sala que se imprime
                    if door.lane == 1:  # Si izquierda
                        b = 0
                        pygame.draw.rect(display, green, (b, door.pos, 60, 60))
                    elif door.lane == 2:  # Si derecha
                        b = displayWidth - 60
                        pygame.draw.rect(display, green, (b, door.pos, 60, 60))
                    elif door.lane == 3:  # Arriba
                        b = 0
                        pygame.draw.rect(display, green, (door.pos, b, 60, 60))
                    else:  # Abajo
                        b = displayHeight - 60
                        pygame.draw.rect(display, green, (door.pos, b, 60, 60))
                    #print('imprimiendo:', b, door.pos)
            #for d in m.doors:  # Verifica en que linea esta para asignarlo a un borde
            #Objetos
            for o in m.obstacles:
                pygame.draw.circle(display, blue, (o.posx, o.posy), 10)
            if m.powerUps != None:
                pygame.draw.rect(display, red, (m.powerUps.posx, m.powerUps.posy, 20, 20))


            message_display('Sala ' + str(n), 'freesansbold.ttf', 20, 50, 50)
            print('mostrando sala:', m.id)
            n += 1
            pygame.display.update()
            time.sleep(1.5)


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


def main():
    pygame.init()
    pygame.display.set_caption('The game')
    intro()


if __name__ == "__main__":
    main()
