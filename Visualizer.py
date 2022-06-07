from __future__ import annotations

import random

import pygame
from SecretColors import Palette
from pygame.surface import SurfaceType, Surface
from pygame.time import Clock

from Barrier import Barrier
from Robot import Robot
from Station import Station
from Strategy import Strategy


class Visualizer:
    palette = Palette("material")
    FPS = 60
    screen: Surface | SurfaceType
    clock: Clock
    randomBackground = random.choice(
        [palette.purple(), palette.indigo(), palette.lime(), palette.cyan(), palette.orange(), palette.yellow(),
         palette.blue(), palette.amber(), palette.white(), palette.violet()])

    def __init__(self, WIDTH, HEIGHT):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Robot Amputator")
        self.clock = pygame.time.Clock()

    def visualize(self, strategy: Strategy, robot: Robot, barriers: [Barrier], station: Station):
        running = True
        i = 0
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.randomBackground)
            strategy.update_and_get_state()
            pygame.draw.circle(self.screen, self.palette.green(), (station.x, station.y), robot.radius // 2)
            pygame.draw.circle(self.screen, self.palette.green(), (station.x, station.y), robot.radius // 2 + i,
                               width=1)
            pygame.draw.circle(self.screen, self.palette.black(), (station.x, station.y), robot.radius // 2, width=1)
            i = (i + 0.3) % 10
            # pygame.draw.line(self.screen, self.palette.gray(), robot.get_view_vector()[0], robot.get_view_vector()[1], 2)
            pygame.draw.circle(self.screen, self.palette.gray_cool(), (robot.x, robot.y), robot.radius)
            pygame.draw.circle(self.screen, self.palette.black(), robot.get_pomp_coord(), robot.radius // 4)
            pygame.draw.circle(self.screen, self.palette.black(), (robot.x, robot.y), robot.radius, width=1)

            for bar in barriers:
                for wall in bar.walls:
                    pygame.draw.line(self.screen, self.palette.black(), wall.start_point, wall.finish_point, 3)

            pygame.display.flip()
        pygame.quit()
