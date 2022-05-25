import logging
import math

import Robot
import Station
import Barrier

FORWARD_STEP = 1
LEFT_ROTATE = -math.pi / 10


class Strategy:
    robot: Robot
    station: Station
    barriers: [Barrier]

    steps_remaining = 0

    def __init__(self, robot: Robot, station: Station, barriers: [Barrier]):
        self.robot = robot
        self.station = station
        self.barriers = barriers

    def update(self):
        if self.robot.on_station(self.station):
            # print("Заряжаюсь...")
            return
        if self.steps_remaining > 0:
            self.steps_remaining -= FORWARD_STEP
            self.robot.forward(FORWARD_STEP)
            print("Вперед")
            return
        else:
            check_res = self.robot.check_front(self.barriers)
            self.steps_remaining = min(check_res, self.robot.view_distance) // FORWARD_STEP

        if self.steps_remaining < self.robot.radius // FORWARD_STEP:
            self.robot.rotate(LEFT_ROTATE)
            print("Налево")
            return

    def update_and_get_state(self):
        self.update()
        return Robot.RobotState(self.robot, self.station)
