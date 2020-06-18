from setings_window import Settings
from robot import Robot2
from sandbox_func import *


def run_window():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    settings = Settings()
    background_image = pygame.image.load('images/450px-Degree-Radian_Conversion.svg.png')
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Test pool")
    robot = Robot2(screen)
    robot_group = pygame.sprite.RenderPlain(robot)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        check_events(robot)
        screen.blit(background_image, [0, 0])
        robot_group.update()

        screen.fill(settings.bg_color)
        screen.blit(background_image, [10, 0])
        robot_group.draw(screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        #update_screen(settings, screen, robot, background_image)

        #print(robot.angle)



run_window()
