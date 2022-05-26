import math
import time

import Robot
import Station
import Barrier


FORWARD_STEP = 1
LEFT_ROTATE = -math.pi / 10


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
            # print("Заряжаюсь...")
            return
        if min(self.robot.check_front(self.barriers)) > self.robot.view_distance/2:
            self.robot.forward(FORWARD_STEP)
            print("Вперед")
            return
        else:
            self.robot.rotate(self.robot.get_angle_to_station(self.station))
            print("Налево")
            return

    def update_and_get_state(self):
        start_time = time.time()
        self.update()
        print(time.time() - start_time)
        return Robot.RobotState(self.robot, self.station)
