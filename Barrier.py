

class Wall:
    start_point: list[float]  # пример точки старта: [x1,y1]
    finish_point: list[float]  # [x2,y2]

    # Wall([x1,y1],[x2,y2])
    def __init__(self, start_point, finish_point):
        self.finish_point = finish_point
        self.start_point = start_point


class Barrier:
    walls: list[Wall]

    def __init__(self, walls):
        self.walls = walls
