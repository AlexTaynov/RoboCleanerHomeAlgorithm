from __future__ import annotations
import threading

import pygame
from pygame.surface import SurfaceType, Surface
from pygame.time import Clock

from Barrier import Barrier
from Robot import RobotState
from Station import Station

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Visualizer:
    WIDTH = 360
    HEIGHT = 480
    FPS = 60
    LOADING_FPS = 3
    screen: Surface | SurfaceType
    clock: Clock

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()

    def visualize(self, robot_states: [RobotState], barriers: [Barrier], station: Station):
        running = True
        iter_number = 0
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)

            robot = robot_states[iter_number]

            pygame.draw.circle(self.screen, BLUE, (robot.x, robot.y), robot.radius)
            pygame.draw.circle(self.screen, RED, (station.position.x, station.position.y), robot.radius // 4)
            # pygame.draw.line(screen, BLUE, robot.get_view_vector().p1, robot.get_view_vector().p2, 5)
            for bar in barriers:
                pnts = []
                for wall in bar.walls:
                    pygame.draw.line(self.screen, GREEN, wall.start_point, wall.finish_point, 5)

            pygame.display.flip()
            if iter_number < len(robot_states) - 1:
                iter_number += 1
        pygame.quit()

    def calc(self, states, data_loader):
        while True:
            state = data_loader()
            states.append(state)
            if state.is_stop():
                return

    def load_data(self, data_loader):
        font = pygame.font.SysFont('Garamond', 30)

        text1 = font.render("Loading.", True, BLACK)
        text2 = font.render("Loading..", True, BLACK)
        text3 = font.render("Loading...", True, BLACK)
        text = [text1, text2, text3]

        textRect = text1.get_rect()
        textRect.center = (self.WIDTH // 2, self.HEIGHT // 2)
        running = True
        i = 0

        states = []

        Event1 = pygame.event.Event(pygame.USEREVENT, attr1='Event1')
        th = threading.Thread(target=self.calc, args=[states, data_loader], daemon=True)
        th.start()

        while running:
            for event in pygame.event.get():
                if event == Event1:
                    running = False
            self.clock.tick(self.LOADING_FPS)
            self.screen.fill(WHITE)
            self.screen.blit(text[i], textRect)
            pygame.display.flip()
            i = (i + 1) % 3

            if not th.is_alive():
                pygame.event.post(Event1)

        th.join()
        return states
