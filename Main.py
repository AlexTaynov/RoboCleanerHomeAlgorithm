# Pygame шаблон - скелет для нового проекта Pygame

from Barrier import *
from Strategy import Strategy
from Robot import Robot
from Station import Station
from Visualizer import Visualizer

if __name__ == "__main__":
    WIDTH = 360
    HEIGHT = 480

    robot = Robot(50, 50, 0, view_distance=30, radius=20)
    w1 = Wall(Point(0, 0), Point(0, HEIGHT))
    w2 = Wall(Point(0, HEIGHT), Point(WIDTH, HEIGHT))
    w3 = Wall(Point(WIDTH, HEIGHT), Point(WIDTH, 0))
    w4 = Wall(Point(WIDTH, 0), Point(0, 0))
    b = [Barrier([w1, w2, w3, w4])]
    st = Station(Point(20, 50))
    strategy = Strategy(robot, st, b)
    visualizer = Visualizer()
    data_loader = lambda: strategy.update_and_get_state()

    robot_states = visualizer.load_data(data_loader)

    visualizer.visualize(robot_states, b, st)
