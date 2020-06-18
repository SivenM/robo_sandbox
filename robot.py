import pygame
import math
from scipy.signal import TransferFunction as transfer_fcn

class Robot2(pygame.sprite.Sprite):
    def __init__(self, screen):
        """Инициализирует робота и задет его начальную позицию"""
        pygame.sprite.Sprite.__init__(self)
        self.direction = 0
        self.screen = screen
        self.scr_image = pygame.image.load('images/tank.png')  # height = 63; width = 50
        self.screen_rect = screen.get_rect()
        self.position = (self.screen_rect.centerx, self.screen_rect.centery)
        self.speed = 0
        self.maxspeed = 1
        self.minspeed = 1
        self.k_right = 0
        self.k_left = 0
        self.k_up = 0
        self.k_down = 0

    def update(self):
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        if self.speed < -self.minspeed:
            self.speed = -self.minspeed
        self.direction += (self.k_right + self.k_left)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.scr_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # def blitme(self):
    #    """"Отрисовывает робота в текущей позиции."""
    #    self.screen.blit(self.image, self.rect)


class Engine:

    def __init__(self, v_desired: float, w_desired: float, side: str, K: float, l: float) -> None:
        """
        :param v_desired: желаемая линейная скорость
        :param w_desired: желаемая угловая скорость
        :param side: 'right' or 'left'
        :param K: постоянная двигателя
        :param l: расстояние между правым и левым колёсами робота
        """
        self.v_desired = v_desired
        self.w_desired = w_desired
        self.side = side
        self.l = l
        self.v_ref = self._get_v_ref()
        self.Ur = self.v_ref / K
        self.V = self._get_V()

    def _get_v_ref(self) -> float:
        """
        :return: v_ref
        """
        if self.side == 'right':
            return self.v_desired + (self.w_desired * self.l / 2)
        elif self.side == 'left':
            return self.v_desired - (self.w_desired * self.l / 2)

    def _get_V(self):
        """
        :return: V
        """
        pass

