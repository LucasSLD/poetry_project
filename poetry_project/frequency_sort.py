from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    """
    Sort elements of a list by frequency of apparition in the input array.
    Args:
        items (list[str  |  int]): Input array to sort

    Returns:
        Iterable[str | int]: list sorted by frequency
    """
    count = {}
    position = {}
    for i, e in enumerate(items):
        if e in count:
            count[e] += 1
        else:
            count[e] = 0
        if e not in position:
            position[e] = i

    def sort_key(i: str | int):
        return (1 / (count[i] + 1), position[i])

    return sorted(items, key=sort_key)
