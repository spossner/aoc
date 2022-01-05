from itertools import chain

from aoc import Rect, Point


def test_rect():
    r1 = Rect(5, 5, 30, 30)
    r2 = Rect(15, 15, 30, 30)
    r3 = Rect(15, 15, 30, 30)
    assert r1 != r2
    assert r2 == r3
    assert r1.contains(r2) is False
    assert r2.contains(r3) is True
    assert r1.contains_point(5, 5)
    assert r1.contains_point(34, 34)
    assert r1.contains_point(35, 35) is False


def test_extend():
    r1 = Rect(5, 5, 10, 10)
    p_out = (Point(3, 3), Point(15, 5), Point(5, 15), Point(15, 15), Point(0, 0), Point(23, 34), Point(23, 2), Point(20, 34))
    p_still_out = (Point(-1, 3), Point(15, -1), Point(24, 15), Point(20, 35))
    p_in = (Point(5, 5), Point(6, 5), Point(14, 5), Point(5, 14), Point(14, 14))
    for p in p_in:
        assert r1.contains_point(*p), "{p} should be inside {r1}"
    for p in chain(p_out, p_still_out):
        assert not r1.contains_point(*p), "{p} should not be inside {r1}"
    for p in p_out:
        r1.extend(*p)
    for p in p_in:
        assert r1.contains_point(*p), "{p} should be inside {r1}"
    for p in p_out:
        assert r1.contains_point(*p), "{p} should now be inside {r1}"
    for p in p_still_out:
        assert not r1.contains_point(*p), "{p} should still not be inside {r1}"


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
