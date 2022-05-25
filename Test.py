from Barrier import Wall, Barrier
from sympy import Point
from Robot import Robot
from Station import Station
import math

if __name__ == "__main__":
    r = Robot(1, 1, 0, 5, 1)
    r.rotate(math.pi / 2)  # +
    r.forward(1)  # +
    print(r.x)  # +
    print(r.y)  # +
    print(r.angle)  # +

    # print('//////')

    st = Station(Point(-10, 1))  # +

    print(r.get_view_vector())  # +
    print(r.get_angle_to_station(st))  # + возвращаем float
    r.rotate(r.get_angle_to_station(st))
    print(r.get_angle_to_station(st))

    r1 = Robot(6, 2, 0, 5, 1)
    w1 = Wall(Point(5, -1), Point(5, 1))
    w2 = Wall(Point(5, 1), Point(7, 0))
    w3 = Wall(Point(5, -1), Point(7, 0))
    b = Barrier([w1, w2, w3])

    # print(b.walls)
    print(r1.check_front([b]))  # +

    print(r1.on_station(Station(Point(2, 0.05))))
