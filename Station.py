from sympy import Point


class Station:
    position: Point

    def __init__(self, point: Point):
        self.position = point
