from JSON_util import JSON_util
from Strategy import Strategy
from Robot import Robot
from Visualizer import Visualizer

if __name__ == "__main__":
    WIDTH = 854
    HEIGHT = 480

    robot = Robot(840, 470, 0, view_distance=15, radius=15)
    mapper = JSON_util("map.json")
    st = mapper.get_station()
    b = mapper.get_barriers()

    strategy = Strategy(robot, st, b)
    visualizer = Visualizer(WIDTH, HEIGHT)
    visualizer.visualize(strategy, robot, b, st)
