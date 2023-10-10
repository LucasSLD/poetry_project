from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    """Flatten the list given as input"""
    l = []
    for e in array:
        if isinstance(e,list):
            l += flat_list(e)
        else:
            l.append(e)
    return l

