from pygame.sprite import Sprite
import pygame

#PLATFORM_WIDTH = 30  # ширина платформы
#PLATFORM_HEIGHT = 30  # высота платформы
#PLATFORM_COLOR = (123, 34, 80)  # цвет ппатформы


class Platform(Sprite):
    """ Класс создания платформы """

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load('platform.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
