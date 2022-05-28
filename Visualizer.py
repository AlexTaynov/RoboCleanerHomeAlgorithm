from __future__ import annotations

import pygame
from pygame.surface import SurfaceType, Surface
from pygame.time import Clock

from Barrier import Barrier
from Robot import  Robot
from Station import Station
from Strategy import Strategy

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLEDNO_GREY = (200, 200, 200)


class Visualizer:
    FPS = 60
    screen: Surface | SurfaceType
    clock: Clock

    def __init__(self, WIDTH, HEIGHT):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Robot Amputator")
        self.clock = pygame.time.Clock()

    def visualize(self, strategy: Strategy, robot: Robot, barriers: [Barrier], station: Station):
        running = True
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            strategy.update_and_get_state()
            pygame.draw.line(self.screen, BLEDNO_GREY, robot.get_view_vector()[0], robot.get_view_vector()[1], 2)
            pygame.draw.circle(self.screen, BLUE, (robot.x, robot.y), robot.radius)
            pygame.draw.circle(self.screen, RED, (station.x, station.y), robot.radius // 2)

            for bar in barriers:
                for wall in bar.walls:
                    pygame.draw.line(self.screen, GREEN, wall.start_point, wall.finish_point, 5)

            pygame.display.flip()
        pygame.quit()
