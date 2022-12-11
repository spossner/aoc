from aoc import get_ints, fetch, batched


def test_fetch():
    assert list(fetch([3], 2)) == [3, None]
    assert list(fetch([3], 2, 0)) == [3, 0]
    assert list(fetch([3, 4], 2)) == [3, 4]
    assert list(fetch([3, 4, 5], 2)) == [3, 4]
    assert list(fetch([3, 4, 5], 10, 0)) == [3, 4, 5, 0, 0, 0, 0, 0, 0, 0]


def test_get_ints():
    assert get_ints("Set value to 2 and jump -34.") == [2, -34]


def test_batched():
    assert list(batched("ABCDEFG", 3)) == [['A','B','C'], ['D','E','F'],['G']]