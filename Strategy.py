import math
import random
import time

import Robot
import Station
import Barrier

FORWARD_STEP = 1
LEFT_ROTATE = -math.pi / 180
RIGHT_ROTATE = math.pi / 180


def to_degree(radians):
    return radians * 180 / math.pi


def to_radians(degree):
    return degree * math.pi / 180


class Strategy:
    robot: Robot
    forward_cnt: int = 0
    flag: int = 1
    reverse_rotate: int = 1
    turn_over_cnt: int = 0
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

        print(to_degree(self.turn_over_cnt))

        if self.robot.on_station(self.station):
            return

        if abs(abs(to_degree(self.turn_over_cnt)) - 720) < 0.5:
            self.reverse_rotate = -1
            self.turn_over_cnt = 0

        if abs(to_degree(self.turn_over_cnt)) - 720 > 0.5:
            self.turn_over_cnt = 0

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

        if (self.forward_cnt > self.robot.radius * 2 + 1) and abs(self.robot.get_angle_to_station(self.station)) > (
                1e-10):
            rotate_angle = self.robot.get_angle_to_station(self.station)
            if rotate_angle > 0:
                rotate_angle = min(rotate_angle, self.reverse_rotate * to_radians(75))
            else:
                rotate_angle = max(rotate_angle, self.reverse_rotate * to_radians(-75))
            self.reverse_rotate = 1
            self.forward_cnt = 0
            self.flag = 0
            self.turn_over_cnt += rotate_angle
            self.robot.rotate(rotate_angle)
            return

        if min(view_barriers_distances) > self.robot.radius * 0.9:
            self.robot.forward(FORWARD_STEP)
            self.rotateCnt = 0
            self.forward_cnt += self.flag
            return

        else:
            self.touchWall = True
            rotate_angle = self.robot.get_angle_to_station(self.station)
            if abs(to_degree(rotate_angle)) > 130:
                self.robot.rotate(rotate_angle)
                self.turn_over_cnt += rotate_angle
                self.prevRotate = 0
                self.flag = 1
                return

            if view_barriers_distances[0] <= view_barriers_distances[-1]:
                self.rotateCnt += 1
                self.robot.rotate(RIGHT_ROTATE)
                self.turn_over_cnt += RIGHT_ROTATE
                self.prevRotate = 1
            else:
                self.robot.rotate(LEFT_ROTATE)
                self.turn_over_cnt += LEFT_ROTATE
                self.prevRotate = -1
            self.rotateCnt += 1
            self.flag = 1
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

        if self.robot.radius * 0.9 < min(view_barriers_distances):
            self.robot.forward(FORWARD_STEP)
            self.rotateCnt = 0
            self.prevRotate = 0
            return

        if self.prevRotate != 0:
            rotate_angle = LEFT_ROTATE if self.prevRotate == -1 else RIGHT_ROTATE
            self.turn_over_cnt += rotate_angle
            self.robot.rotate(rotate_angle)
            return

        if view_barriers_distances[0] > self.robot.view_distance and view_barriers_distances[
            -1] > self.robot.view_distance:
            self.robot.rotate(LEFT_ROTATE)
            self.turn_over_cnt += LEFT_ROTATE
            self.prevRotate = -1
            return
        # if self.rotateCnt > 30:
        #     self.rotateCnt = 0
        #     self.touchWall = False
        #     return

        if view_barriers_distances[0] <= view_barriers_distances[-1]:
            self.rotateCnt += 1
            self.robot.rotate(RIGHT_ROTATE)
            self.turn_over_cnt += RIGHT_ROTATE
            self.prevRotate = 1
        else:
            self.robot.rotate(LEFT_ROTATE)
            self.turn_over_cnt += LEFT_ROTATE
            self.prevRotate = -1
