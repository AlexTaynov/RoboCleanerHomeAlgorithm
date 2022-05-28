import math
import time

import Robot
import Station
import Barrier

FORWARD_STEP = 1
LEFT_ROTATE = -math.pi / 50
RIGHT_ROTATE = math.pi / 45


class Strategy:
    robot: Robot
    station: Station
    barriers: [Barrier]
    touchWall: bool = False
    rotateCnt: int = 0

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

        if self.rotateCnt > 10:
            self.robot.rotate(3 * LEFT_ROTATE)
            self.rotateCnt = 0
            return

        if min(self.robot.check_front(self.barriers)) > self.robot.view_distance / 4:
            self.robot.forward(FORWARD_STEP)
            self.rotateCnt = 0
            print("Вперед")
            return

        else:
            self.touchWall = True
            self.robot.rotate(self.robot.get_angle_to_station(self.station))
            self.rotateCnt += 1
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
            self.robot.rotate(LEFT_ROTATE)
            self.touchWall = False
            return

        if min(view) > self.robot.view_distance / 4:
            self.robot.forward(FORWARD_STEP)
            print("Вперед")
            self.rotateCnt = 0
            return

        if self.rotateCnt > 20:
            self.rotateCnt = 0
            self.touchWall = False
            return

        if view[0] <= view[2]:
            self.rotateCnt += 1
            self.robot.rotate(RIGHT_ROTATE)
        else:
            self.robot.rotate(LEFT_ROTATE)
