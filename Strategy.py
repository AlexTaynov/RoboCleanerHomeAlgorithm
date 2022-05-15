import math

import Robot
import Station
import Barrier

FORWARD_STEP = 0.5
LEFT_ROTATE = math.pi / 2


class Strategy:
    robot: Robot
    station: Station
    barriers: [Barrier]

    def __init__(self, robot: Robot, station: Station, barriers: [Barrier]):
        self.robot = robot
        self.station = station
        self.barriers = barriers

    def update(self):
        if self.robot.on_station(self.station):
            print("Заряжаюсь...")
            return
        if self.robot.check_front(self.barriers) == -1:
            self.robot.forward(FORWARD_STEP)
            print("Вижу цель, не вижу препятствий...")
            return
        else:
            self.robot.rotate(LEFT_ROTATE)
            print("Эх.. Впереди преграда. Иду налево")
            return
