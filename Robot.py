import math
from sympy import Point, Line, Segment

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
        view_segment = self.get_view_vector()
        retval = 1000000000
        for barrier in barriers:
            for wall in barrier.walls:
                b_segment = Segment(Point(wall.start_point), Point(wall.finish_point))
                points: [Point] = view_segment.intersection(b_segment)
                for point in points:
                    retval = min(retval, float(point.distance(Point(self.x, self.y))))

        return retval

    def get_angle_to_station(self, station: Station):
        toStationVec = Line(Point(self.x, self.y), station.position)
        return float(toStationVec.angle_between(self.get_view_vector()))

    def get_view_vector(self):
        return Segment(Point(self.x, self.y), Point(self.x + math.cos(self.angle) * self.view_distance,
                                                    self.y + math.sin(self.angle) * self.view_distance))

    def on_station(self, station: Station) -> bool:
        return Point(self.x, self.y).distance(station.position) <= self.radius
