from Barrier import Wall, Barrier
from sympy import Point
from Robot import Robot
from Station import Station
import math
import json


def fromJSON(data: dict):
    st_json = Station(data)
    #print(st_json.position)
    barriers = []
    #print(data["barriers"][0]["walls"])
    # for barrier in data
    for i in range(len(data["barriers"])):
        walls_for_barrier = []
        for w in data["barriers"][i]["walls"]:
            walls_for_barrier.append(Wall(Point(w["start_point"]["x"], w["start_point"]["y"]),
                                          Point(w["finish_point"]["x"], w["finish_point"]["y"])))
        barriers.append(Barrier(walls_for_barrier))
    #print(barriers)
    #print(barriers[0].walls[1].finish_point)#Пример
    return st_json, barriers




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

    r1 = Robot(2, 0, 0, 5, 1)
    w1 = Wall(Point(5, -1), Point(5, 1))
    w2 = Wall(Point(5, 1), Point(7, 0))
    w3 = Wall(Point(5, -1), Point(7, 0))
    b = Barrier([w1, w2, w3])

    # print(b.walls)
    print(r1.check_front([b]))  # +

    print(r1.on_station(Station(Point(2, 0.05))))

    print('//////Для JSON ниже')


    with open('map.json') as json_file:
        data = json.load(json_file)
    print(data)
    station_and_barriers = fromJSON(data)
    print(station_and_barriers[0].position)
    print(station_and_barriers[1][0].walls[1].finish_point)

    # # print(type(data))
    # # print(data["station"]["x"])
    # # print(data["barriers"][1]["walls"][0])
    #
    # st_json = Station(data)
    # print(st_json.position)
    # print('/////')
    # barriers = []
    # print(data["barriers"][0]["walls"])
    # #for barrier in data
    # for i in range(len(data["barriers"])):
    #     walls_for_barrier = []
    #     for w in data["barriers"][i]["walls"]:
    #         walls_for_barrier.append(Wall(Point(w["start_point"]["x"], w["start_point"]["y"]),
    #                                  Point(w["finish_point"]["x"], w["finish_point"]["y"])))
    #     barriers.append(Barrier(walls_for_barrier))
    # print(barriers)
    # print(barriers[0].walls[1].finish_point)#Пример


