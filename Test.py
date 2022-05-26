import math

from Barrier import Wall, Barrier
from Robot import Robot
from Station import Station

if __name__ == "__main__":
    r = Robot(1, 1, 0, 5, 1)
    r.rotate(math.pi / 2)  # +
    r.forward(1)  # +
    print(r.x)  # +
    print(r.y)  # +
    print(r.angle)  # +
    assert (r.angle == math.pi / 2 and r.x == 1 and r.y == 2)

    print('//////')

    st = Station(1.5, -1.5)  # +
    print(r.get_view_vector())  # +
    print(r.get_angle_to_station(st))  # + возвращаем float
    r.rotate(r.get_angle_to_station(st))
    print(r.get_angle_to_station(st))
    assert (st.x == 1.5 and st.y == 1.5 and r.get_angle_to_station(st) == 0)

    r1 = Robot(7, 1, -math.pi/2, 5, 2)
    w1 = Wall([5, -1], [5, 1])
    w2 = Wall([5, 1], [7, 0])
    w3 = Wall([5, -1], [7, 0])
    b = Barrier([w1, w2, w3])

    # print(b.walls)
    print(r1.check_front([b]))  # +

    print(r1.on_station(Station(2, 0.05)))
