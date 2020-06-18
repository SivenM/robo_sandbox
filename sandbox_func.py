import pygame
import sys


def check_events(robot):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, robot)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, robot)


def check_keydown_events(event, robot):
    """Реагирует на нажатие клавиш"""
    down = event.type == pygame.KEYDOWN
    if event.key == pygame.K_UP:
        robot.maxspeed = 1
        robot.k_up = down * 0.1
    elif event.key == pygame.K_DOWN:
        robot.minspeed = 1
        robot.k_down = down * -0.1
    elif event.key == pygame.K_LEFT:
        robot.k_left = down * 1
    elif event.key == pygame.K_RIGHT:
        robot.k_right = down * -1
    elif event.key == pygame.K_ESCAPE:
        sys.exit(0)


def check_keyup_events(event,robot):
    """Реагирует на отжатие клавиши"""
    if event.key == pygame.K_UP:
        robot.maxspeed  = 0
        robot.k_up = 0
    elif event.key == pygame.K_DOWN:
        robot.minspeed = 0
        robot.k_down = 0
    elif event.key == pygame.K_LEFT:
        robot.k_left = 0
    elif event.key == pygame.K_RIGHT:
        robot.k_right = 0


def update_screen(settings, screen, robot, background_image):
    screen.fill(settings.bg_color)
    #robot.blitme()
    screen.blit(background_image, [10, 0])
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


"""class Display:
    def __init__(self,):
        self.map = self.create_map()

    def create_map(self):


class Map:
    """