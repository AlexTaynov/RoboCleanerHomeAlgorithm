
class Wall:
    start_point: [float]
    finish_point: [float]

    # Wall(Point(x1,y1),Point(x2,y2))
    def __init__(self, start_point, finish_point):
        self.finish_point = finish_point
        self.start_point = start_point


class Barrier:
    walls: [Wall]

    def __init__(self, walls):
        self.walls = walls
