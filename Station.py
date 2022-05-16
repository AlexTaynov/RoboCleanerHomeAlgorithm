from sympy import Point
import json


class Station:
    position: Point

    def __init__(self, *args):
        if isinstance(args[0], Point):
            self.position = args[0]
        elif isinstance(args[0], dict):
            self.position = Point(args[0]["station"]["x"], args[0]["station"]["y"])
