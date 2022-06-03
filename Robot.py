import math

import Barrier
from Station import Station
import util


class Robot:
    x: float
    y: float
    angle: float
    view_distance: float
    radius: float

    def __init__(self, x, y, angle, view_distance, radius):
        self.y = y
        self.x = x
        self.angle = angle
        self.view_distance = view_distance + radius
        self.radius = radius

    def forward(self, dist):
        self.y += math.sin(self.angle) * dist
        self.x += math.cos(self.angle) * dist

    def rotate(self, angle):
        self.angle += angle

    def __check_front__(self, phi: float, barriers: [Barrier]) -> float:
        retval = 1000000000
        for barrier in barriers:
            for wall in barrier.walls:
                p1, p2 = wall.start_point, wall.finish_point
                p3, p4 = [self.x, self.y], [self.x + math.cos(self.angle + phi) * self.view_distance,
                                            self.y + math.sin(self.angle + phi) * self.view_distance]
                point = util.intersection(p1, p2, p3, p4)
                if point:
                    retval = min(retval, distance(point, [self.x + math.cos(self.angle) * self.radius,
                                                          self.y + math.sin(self.angle) * self.radius]))
        return retval

    def check_front(self, barriers: [Barrier]):
        return self.__check_front__(-math.pi / 4, barriers), \
               self.__check_front__(0, barriers), \
               self.__check_front__(math.pi / 4, barriers)

    def get_angle_to_station(self, station: Station):
        x, y = matrix_rotate(station.x - self.x, station.y - self.y, -self.angle)
        return math.atan2(y, x)

    def get_view_vector(self):
        return [[self.x, self.y], [self.x + math.cos(self.angle) * self.view_distance,
                                   self.y + math.sin(self.angle) * self.view_distance]]

    def get_pomp_coord(self):
        return [self.x - math.cos(self.angle) * self.radius // 2,
                self.y - math.sin(self.angle) * self.radius // 2]

    def on_station(self, station: Station) -> bool:
        return distance([station.x, station.y], [self.x, self.y]) <= self.radius


def distance(p1: list, p2: list):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def matrix_rotate(x, y, phi):
    return x * math.cos(phi) - y * math.sin(phi), \
           x * math.sin(phi) + y * math.cos(phi)


class RobotState:
    x: float
    y: float
    angle: float
    view_distance: float
    radius: float
    view_vector: [[float]]
    onStation: bool

    def __init__(self, robot: Robot, st: Station):
        self.x = robot.x
        self.y = robot.y
        self.angle = robot.angle
        self.view_distance = robot.view_distance
        self.radius = robot.radius
        self.view_vector = robot.get_view_vector()
        self.onStation = robot.on_station(st)

    def is_stop(self):
        return self.onStation
