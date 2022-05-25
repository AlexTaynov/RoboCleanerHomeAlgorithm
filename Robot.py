import math
from sympy import Point, Line, Segment
import poly_point_isect

import Barrier
from Station import Station


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
        self.view_distance = view_distance
        self.radius = radius

    def forward(self, dist):
        self.y += math.sin(self.angle) * dist
        self.x += math.cos(self.angle) * dist

    def rotate(self, angle):
        self.angle += angle

    def check_front(self, barriers: [Barrier]) -> float:
        retval = 1000000000
        segments = []
        for barrier in barriers:
            for wall in barrier.walls:
                segments.append(wall.start_point.coordinates)
                segments.append(wall.finish_point.coordinates)
        points1 = poly_point_isect.isect_polygon(segments)
        segments.append((self.x, self.y))
        segments.append(
            (self.x + math.cos(self.angle) * self.view_distance, self.y + math.sin(self.angle) * self.view_distance))
        points2 = poly_point_isect.isect_polygon(segments)
        points2 = list(set(points2) - set(points1))
        for point in points2:
            retval = min(retval, ((point[0] - self.x) ** 2 + (point[1] - self.y) ** 2) ** 0.5)
        return retval

    def get_angle_to_station(self, station: Station):
        toStationVec = Line(Point(self.x, self.y), station.position)
        return float(toStationVec.angle_between(self.get_view_vector()))

    def get_view_vector(self):
        return Segment(Point(self.x, self.y), Point(self.x + math.cos(self.angle) * self.view_distance,
                                                    self.y + math.sin(self.angle) * self.view_distance))

    def on_station(self, station: Station) -> bool:
        return Point(self.x, self.y).distance(station.position) <= self.radius


class RobotState:
    x: float
    y: float
    angle: float
    view_distance: float
    radius: float
    view_vector: Segment
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
