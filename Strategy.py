import math
import time

import Robot
import Station
import Barrier

FORWARD_STEP = 1
LEFT_ROTATE = -math.pi / 20
RIGHT_ROTATE = math.pi / 15


class Strategy:
    robot: Robot
    station: Station
    barriers: [Barrier]
    touchWall: bool = False

    def __init__(self, robot: Robot, station: Station, barriers: [Barrier]):
        self.robot = robot
        self.station = station
        self.barriers = barriers

    def update(self):
        if self.robot.on_station(self.station):
            # print("Заряжаюсь...")
            return

        if self.touchWall:
            self.goTouchingWall()
            return

        if min(self.robot.check_front(self.barriers)) > self.robot.view_distance / 2:
            self.robot.forward(FORWARD_STEP)
            print("Вперед")
            return

        else:
            self.touchWall = True
            self.robot.rotate(self.robot.get_angle_to_station(self.station))
            print("Налево")
            return

    def update_and_get_state(self):
        start_time = time.time()
        self.update()
        print(time.time() - start_time)
        return Robot.RobotState(self.robot, self.station)

    def goTouchingWall(self):
        view = self.robot.check_front(self.barriers)

        if view[0] > self.robot.view_distance and view[2] > self.robot.view_distance:
            self.touchWall = False
            return

        if view[1] > self.robot.view_distance / 4:
            self.robot.forward(FORWARD_STEP)
            print("Вперед")
            return

        if view[0] <= view[2]:
            self.robot.rotate(RIGHT_ROTATE)
        else:
            self.robot.rotate(LEFT_ROTATE)

        # if view[0] >= self.robot.view_distance / 2:
        #     self.robot.rotate(RIGHT_ROTATE)
        #     return
        #
        # if view[2] >= self.robot.view_distance / 2:
        #     self.robot.rotate(LEFT_ROTATE)
        #     return
