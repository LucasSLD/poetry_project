from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    count = {}
    position = {}
    for i in range(len(items)):
        e = items[i]
        if e in count.keys():
            count[e] += 1
        else:
            count[e] = 0
        if e not in position.keys():
            position[e] = i
    def sort_key(i : str | int): return (1/(count[i]+1),position[i])
    return sorted(items,key=sort_key)