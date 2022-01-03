from aoc import *

if __name__ == '__main__':
    assert rot_cw(Point(0, 1)) == (-1, 0)
    assert rot_ccw(Point(0, 1)) == (1, 0)
    assert rot_ccw(Point(1, 0)) == (0, -1)

    assert manhattan_distance((1, 2, -3)) == 6
    assert manhattan_distance(Point3d(1, 2, -3)) == 6
    assert manhattan_distance(Point(-2, -4)) == 6

    assert extract_ints("Set value to 2 and jump -34.") == [2, -34]
