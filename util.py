
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def sps(s1: [float], s2: [float]):
    return s1[0] * s2[0] + s1[1] * s2[1]


def intersection(p1, p2, p3, p4):
    L1 = line(p1, p2)
    L2 = line(p3, p4)
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        if sps([p1[0] - x, p1[1] - y], [p2[0] - x, p2[1] - y]) <= 0 and sps([p3[0] - x, p3[1] - y],
                                                                            [p4[0] - x, p4[1] - y]) <= 0:
            return x, y
    return False
