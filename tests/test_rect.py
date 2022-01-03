from aoc import Rect, Point

def test_rect():
    r1 = Rect(5, 5, 30, 30)
    r2 = Rect(15, 15, 30, 30)
    r3 = Rect(15,15,30,30)
    assert r1 != r2
    assert r2 == r3
    assert r1.contains(r2) is False
    assert r2.contains(r3) is True
    assert r1.contains_point(5,5)
    assert r1.contains_point(34,34)
    assert r1.contains_point(35,35) is False


def test_rect_intersection():
    r1 = Rect(5, 5, 30, 30)
    r2 = Rect(15, 15, 30, 30)
    r_i = r1.intersection(r2)
    r_j = r2.intersection(r1)
    assert r1.contains(r_i) is True
    assert r1.contains(r_j) is True
    assert r2.contains(r_i) is True
    assert r2.contains(r_j) is True
    assert r_i.contains(r_i) is True
    assert r_i.contains(r_j) is True
    assert r_j.contains(r_i) is True
    assert r_j.contains(r_j) is True
    assert r_i == r_j
