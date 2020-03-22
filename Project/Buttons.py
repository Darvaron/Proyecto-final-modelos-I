import pygame

from Project import Main

class Buttons():
    def __init__(self, img1, img2, x, y, display, act=None):
        self.normal_image = img1
        self.selec_image = img2
        self.act_image = self.normal_image
        self.rect = self.act_image.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.display = display
        self.act = act

    def update(self):
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(pygame.mouse.get_pos()):  # Efecto HOVER
            self.act_image = self.selec_image
            if click[0] == 1 and self.act != None:
                self.act()
        else:
            self.act_image = self.normal_image

        self.display.blit(self.act_image, self.rect)


