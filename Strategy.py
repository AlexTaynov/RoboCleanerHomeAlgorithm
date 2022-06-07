import math
import time

import Robot
import Station
import Barrier

FORWARD_STEP = 1
LEFT_ROTATE = -math.pi / 180
RIGHT_ROTATE = math.pi / 180


class Strategy:
    robot: Robot
    station: Station
    barriers: [Barrier]
    touchWall: bool = False
    rotateCnt: int = 0
    lastRotate: int = 0

    def __init__(self, robot: Robot, station: Station, barriers: [Barrier]):
        self.robot = robot
        robot.rotate(robot.get_angle_to_station(station))
        self.station = station
        self.barriers = barriers

    def update(self):
        if self.robot.on_station(self.station):
            return

        if self.touchWall:
            self.goTouchingWall()
            return

        # if self.rotateCnt > 10:
        #     self.robot.rotate(math.pi / 2)
        #     self.rotateCnt = 0
        #     return

        view = self.robot.check_front(self.barriers)

        # if min(view) > self.robot.radius and self.lastRotate == 10:
        #     self.robot.rotate(self.robot.get_angle_to_station(self.station))
        #     return

        if min(view) > self.robot.radius:
            self.robot.forward(FORWARD_STEP)
            self.rotateCnt = 0
            return

        else:
            self.touchWall = True
            self.lastRotate = 0
            self.robot.rotate(self.robot.get_angle_to_station(self.station))
            self.rotateCnt += 1
            return

    def update_and_get_state(self):
        start_time = time.time()
        self.update()
        print(time.time() - start_time)
        return Robot.RobotState(self.robot, self.station)

    def goTouchingWall(self):
        view = self.robot.check_front(self.barriers)

        if min(view) > self.robot.view_distance and self.lastRotate == 0:
            self.touchWall = False
            self.lastRotate = 10
            return

        if self.robot.radius < min(view):
            self.robot.forward(FORWARD_STEP)
            self.rotateCnt = 0
            self.lastRotate = 0
            return

        if self.lastRotate != 0:
            self.robot.rotate(LEFT_ROTATE if self.lastRotate == -1 else RIGHT_ROTATE)
            return

        if view[0] > self.robot.view_distance and view[2] > self.robot.view_distance:
            self.robot.rotate(LEFT_ROTATE)
            self.lastRotate = -1
            return
        # if self.rotateCnt > 30:
        #     self.rotateCnt = 0
        #     self.touchWall = False
        #     return

        if view[0] <= view[2]:
            self.rotateCnt += 1
            self.robot.rotate(RIGHT_ROTATE)
            self.lastRotate = 1
        else:
            self.robot.rotate(LEFT_ROTATE)
            self.lastRotate = -1
