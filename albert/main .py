import pygame
import sys
from platform import Platform
from robot import Robot

WINDOW = (750, 600)  # window size
BG_COLOR = (0, 0, 0)  # background color (RGB)

PLATFORM_WIDTH = 30  # ширина платформы
PLATFORM_HEIGHT = 30  # высота платформы
PLATFORM_COLOR = (123, 34, 80)  # цвет ппатформы


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    #ico = pygame.image.load('ico/ico_game.ico')
    #pygame.display.set_icon(ico)
    pygame.display.set_caption("Robot Map")  # name window
    bg = pygame.Surface(WINDOW)  # создание видимой поверхности

    bg.fill(BG_COLOR)

    # создание робота
    robot = Robot(50, 60)
    left = right = up = down = False

    # создание карты
    map = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-            --         -",
        "-                       -",
        "--                      -",
        "-                       -",
        "-                   --- -",
        "-                       -",
        "-                       -",
        "-      ---              -",
        "-                       -",
        "-   -----------         -",
        "-                       -",
        "-                -      -",
        "-                   --  -",
        "-                       -",
        "-                       -",
        "-------------------------"]

    sprite_group = pygame.sprite.Group()
    sprite_group.add(robot)
    platforms = []

    x = y = 0
    for row in map:
        for symbol in row:
            if symbol == "-":
                pl = Platform(x, y)
                sprite_group.add(pl)
                platforms.append(pl)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    # таймер
    timer = pygame.time.Clock()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    left = True
                if ev.key == pygame.K_RIGHT:
                    right = True
                if ev.key == pygame.K_UP:
                    up = True
                if ev.key == pygame.K_DOWN:
                    down = True

            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT:
                    left = False
                if ev.key == pygame.K_RIGHT:
                    right = False
                if ev.key == pygame.K_UP:
                    up = False
                if ev.key == pygame.K_DOWN:
                    down = False

        # отображение робота
        robot.update(left, right, up, down)

        # задний фон
        screen.blit(bg, (0, 0))
        sprite_group.draw(screen)
        # обновление экрана
        pygame.display.update()
        # колличество fps (больше фпс быстрее игра, меньше - медленнее)
        timer.tick(60)


if __name__ == "__main__":
    main()
