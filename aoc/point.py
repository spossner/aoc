from collections import namedtuple
from typing import Union

Point = namedtuple('Point', 'x,y', defaults=[0, 0])
Point3d = namedtuple('Point3d', 'x,y,z', defaults=[0, 0, 0])

DIRECT_ADJACENTS = ((0, -1), (-1, 0), (1, 0), (0, 1))  # 4 adjacent nodes
ALL_ADJACENTS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


NORTH = Point(0, -1)
EAST = Point(1, 0)
SOUTH = Point(0, 1)
WEST = Point(-1, 0)

def translate(p: Union[Point, Point3d, tuple], offset: Union[Point, Point3d, tuple]) -> Union[Point, Point3d, tuple]:
    if type(p) == Point:
        return Point(p.x + offset.x, p.y + offset.y)
    if type(p) == Point3d:
        return Point3d(p.x + offset.x, p.y + offset.y, p.z + offset.z)
    if type(p) == tuple:
        assert len(p) == len(offset)
        result = []
        for i in range(len(p)):
            result.append(p[i]+offset[i])
        return tuple(result)
    raise ValueError(f'can not translate {type(p)}')


def rot_cw(p: tuple) -> tuple:
    return Point(-p[1], p[0])


def rot_ccw(p: tuple) -> tuple:
    return Point(p[1], -p[0])


def manhattan_distance(p) -> int:
    return sum(map(abs, p))
