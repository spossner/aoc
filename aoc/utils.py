import re
from itertools import chain


def extract_ints(raw: str) -> list[int]:
    """Utility function to extract all integers from some string.
    Many inputs can be directly parsed with this function.
    """
    return list(map(int, re.findall(r"((?:-|\+)?\d+)", raw)))

def fetch(iterable, n, fillvalue=None):
    """
    fetches n values from iterable - filled with fillvalue if needed;
    great for destructuring data with different number of arguments etc
    :param iterable: the iterable to fetch from
    :param n: the number of elements to fetch; align that with your destructuring
    :param fillvalue: optional fill value if less than n elements are available (None as default)
    :return: list with the n elements; filled with fillvalue if needed
    """
    if len(iterable) >= n:
        return iterable[0:n]
    fill = [fillvalue] * (n - len(iterable))
    return chain(iterable, fill)