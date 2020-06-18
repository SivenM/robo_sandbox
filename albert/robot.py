from pygame.sprite import Sprite
from pygame import Surface

SPEED = 5
ROBOT_WIDTH = 20
ROBOT_HEIGHT = 20
ROBOT_COLOR = (200, 0, 20)


class Robot(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((ROBOT_WIDTH, ROBOT_HEIGHT))  # ширина и высота поверхности
        self.image.fill(ROBOT_COLOR)  # цвет этой поверхности
        self.rect = self.image.get_rect()
        self.rect.x = x  # координаты "робота" по х
        self.rect.y = y  # координаты "робота" по у

    def update(self, left, right, up, down):
        if left:
            self.rect.x -= SPEED
        if right:
            self.rect.x += SPEED
        if up:
            self.rect.y -= SPEED
        if down:
            self.rect.y += SPEED

    def draw(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))
