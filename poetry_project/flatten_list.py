from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    L = []
    for e in array:
        if type(e) is list:
            L += flat_list(e)
        else:
            L.append(e)
    return L