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
    forward_cnt: int = 0
    station: Station
    barriers: [Barrier]
    touchWall: bool = False
    rotateCnt: int = 0
    prevRotate: int = 0

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
            self.forward_cnt = 0
            return

        # if self.rotateCnt > 10:
        #     self.robot.rotate(math.pi / 2)
        #     self.rotateCnt = 0
        #     return

        view_barriers_distances = self.robot.check_front(self.barriers)

        # if min(view) > self.robot.radius and self.lastRotate == 10:
        #     self.robot.rotate(self.robot.get_angle_to_station(self.station))
        #     return

        if (self.forward_cnt > self.robot.radius * 2 + 1) and abs(self.robot.get_angle_to_station(self.station)) > (1e-10):
            rotate_angle = self.robot.get_angle_to_station(self.station)
            if rotate_angle > 0:
                rotate_angle = min(rotate_angle, math.pi / 180 * 90)
            else:
                rotate_angle = max(rotate_angle, math.pi / 180 * 90)
            #print(rotate_angle * 180 / math.pi)
            self.forward_cnt = 0
            self.robot.rotate(rotate_angle)

        if min(view_barriers_distances) > self.robot.radius:
            self.robot.forward(FORWARD_STEP)
            #self.robot.rotate(self.robot.get_angle_to_station(self.station))
            self.rotateCnt = 0
            self.forward_cnt += 1
            return

        else:
            self.touchWall = True
            self.prevRotate = 0
            self.rotateCnt += 1
            return

    def update_and_get_state(self):
        start_time = time.time()
        self.update()
        # print(time.time() - start_time)
        return Robot.RobotState(self.robot, self.station)

    def goTouchingWall(self):
        view_barriers_distances = self.robot.check_front(self.barriers)

        if min(view_barriers_distances) > self.robot.view_distance and self.prevRotate == 0:
            self.touchWall = False
            self.prevRotate = 0
            return

        if self.robot.radius < min(view_barriers_distances):
            self.robot.forward(FORWARD_STEP)
            self.rotateCnt = 0
            self.prevRotate = 0
            return

        if self.prevRotate != 0:
            rotate_angle = LEFT_ROTATE if self.prevRotate == -1 else RIGHT_ROTATE
            self.robot.rotate(rotate_angle)
            return

        if view_barriers_distances[0] > self.robot.view_distance and view_barriers_distances[2] > self.robot.view_distance:
            self.robot.rotate(LEFT_ROTATE)
            self.prevRotate = -1
            return
        # if self.rotateCnt > 30:
        #     self.rotateCnt = 0
        #     self.touchWall = False
        #     return

        if view_barriers_distances[0] <= view_barriers_distances[2]:
            self.rotateCnt += 1
            self.robot.rotate(RIGHT_ROTATE)
            self.prevRotate = 1
        else:
            self.robot.rotate(LEFT_ROTATE)
            self.prevRotate = -1
