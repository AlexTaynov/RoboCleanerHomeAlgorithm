# Pygame шаблон - скелет для нового проекта Pygame
import math

from Barrier import *
from Strategy import Strategy
from Robot import Robot
from Station import Station
from Visualizer import Visualizer

if __name__ == "__main__":
    WIDTH = 360
    HEIGHT = 480

    robot = Robot(50, 50, 0, view_distance=30, radius=20)
    w1 = Wall([0, 0], [0, HEIGHT])
    w2 = Wall([0, HEIGHT], [WIDTH, HEIGHT])
    w3 = Wall([WIDTH, HEIGHT], [WIDTH, 0])
    w4 = Wall([WIDTH, 0], [0, 0])
    w5 = Wall([150, 150], [360, 150])
    w6 = Wall([150, 150], [150, 100])
    w7 = Wall([1, 150], [100, 150])
    w8 = Wall([1, 150], [120, 200])
    w9 = Wall([100, 150], [120, 200])
    w10 = Wall([330, 150], [330, 300])
    w11 = Wall([150, 350], [360, 350])
    b = [Barrier([w1, w2, w3, w4]), Barrier([w5, w6, w7, w8, w9, w10, w11])]
    st = Station(350, 170)
    strategy = Strategy(robot, st, b)
    visualizer = Visualizer(WIDTH, HEIGHT)
    visualizer.visualize(strategy, robot, b, st)
