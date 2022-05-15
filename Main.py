# Pygame шаблон - скелет для нового проекта Pygame
import pygame

from Barrier import *
from Strategy import Strategy
from Robot import Robot
from Station import Station

if __name__ == "__main__":
    WIDTH = 360
    HEIGHT = 480
    FPS = 100

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    robot = Robot(50, 50, 0, view_distance=30, radius=20)
    w1 = Wall(Point(0, 0), Point(0, HEIGHT))
    w2 = Wall(Point(0, HEIGHT), Point(WIDTH, HEIGHT))
    w3 = Wall(Point(WIDTH, HEIGHT), Point(WIDTH, 0))
    w4 = Wall(Point(WIDTH, 0), Point(0, 0))
    b = [Barrier([w1, w2, w3, w4])]
    st = Station(Point(20, 100))
    strategy = Strategy(robot, st, b)

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        strategy.update()

        # Рендеринг

        screen.fill(WHITE)

        pygame.draw.circle(screen, BLUE, (robot.x, robot.y), robot.radius)
        pygame.draw.circle(screen, RED, (st.position.x, st.position.y), robot.radius // 2)
        pygame.draw.line(screen, BLUE, robot.get_view_vector().p1, robot.get_view_vector().p2, 5)
        for bar in b:
            pnts = []
            for wall in bar.walls:
                pygame.draw.line(screen, GREEN, list(wall.start_point), list(wall.finish_point), 5)

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()
