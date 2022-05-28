import json
from Station import Station
from Barrier import Barrier, Wall


class JSON_util:
    data = dict

    def __init__(self, file_name):
        with open(file_name) as json_file:
            self.data = json.load(json_file)

    def get_station(self):
        return Station(self.data["station"]["x"], self.data["station"]["y"])

    def get_barriers(self):
        barriers = []
        for i in range(len(self.data["barriers"])):
            walls_for_barrier = []
            for w in self.data["barriers"][i]["walls"]:
                walls_for_barrier.append(Wall([w["start_point"]["x"], w["start_point"]["y"]],
                                              [w["finish_point"]["x"], w["finish_point"]["y"]]))
            barriers.append(Barrier(walls_for_barrier))
        return barriers
