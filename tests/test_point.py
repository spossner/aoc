from aoc import *

def test_rotation_cw():
    assert rot_cw(Point(0, 1)) == (-1, 0)

def test_rotation_ccw():
    assert rot_ccw(Point(0, 1)) == (1, 0)
    assert rot_ccw(Point(1, 0)) == (0, -1)

def test_length():
    assert length((1, 2, -3)) == 6
    assert length(Point3d(1, 2, -3)) == 6
    assert length(Point(-2, -4)) == 6

def test_manhattan_distance():
    assert manhattan_distance((1, 2, -3), (2,0,-3)) == 3
    assert manhattan_distance(Point3d(1, 2, -3), Point3d(-1,-1,-1)) == 7
    assert manhattan_distance(Point(-2, -4), Point(0,-1)) == 5

def test_adjacents():
    assert list(all_adjacent_iter(Point(12,5))) == [(11, 4), (12, 4), (13, 4), (11, 5), (13, 5), (11, 6), (12, 6), (13, 6)]
    assert list(direct_adjacent_iter(Point(12, 5))) == [(12, 4), (11, 5), (13, 5), (12, 6),]
