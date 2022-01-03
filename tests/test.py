from aoc import *

if __name__ == '__main__':
    assert rot_cw(Point(0, 1)) == (-1, 0)
    assert rot_ccw(Point(0, 1)) == (1, 0)
    assert rot_ccw(Point(1, 0)) == (0, -1)

    assert manhattan_distance((1, 2, -3)) == 6
    assert manhattan_distance(Point3d(1, 2, -3)) == 6
    assert manhattan_distance(Point(-2, -4)) == 6

    assert extract_ints("Set value to 2 and jump -34.") == [2, -34]

    # (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
    p = list(all_adjacent_iter(Point(12,5)))
    assert p == [(11, 4), (12, 4), (13, 4), (11, 5), (13, 5), (11, 6), (12, 6), (13, 6)]

    p = list(direct_adjacent_iter(Point(12, 5)))
    print(p)
    assert p == [(12, 4), (11, 5), (13, 5), (12, 6),]
