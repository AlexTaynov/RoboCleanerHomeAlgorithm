import math
from sympy import Point, Line, Segment

import Barrier


class Robot:
    x: float
    y: float
    angle: float
    view_distance: float

    def __init__(self, x, y, angle, view_distance):
        self.y = y
        self.x = x
        self.angle = angle
        self.view_distance = view_distance

    def forward(self, dist):
        self.y += math.sin(self.angle) * dist
        self.x += math.cos(self.angle) * dist

    def rotate(self, angle):
        self.angle += angle

    def checkFront(self, barriers: list[Barrier]) -> float:
        view_segment = Segment(Point(self.x, self.y), Point(self.x + math.cos(self.angle) * self.view_distance,
                                                            self.y + math.sin(self.angle) * self.view_distance))
        ret_val = 1000000000
        for barrier in barriers:
            for wall in barrier.walls:
                b_segment = Segment(Point(wall.start_point), Point(wall.finish_point))
                points: list[Point] = view_segment.intersection(b_segment)
                for point in points:
                    ret_val = min(ret_val, point.distance(Point(self.x, self.y)))

        if ret_val == 1000000000:
            return -1
        return ret_val
