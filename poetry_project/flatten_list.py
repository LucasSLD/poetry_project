from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    """
        Flatten list given as input
    Args:
        array (list[int]): The array to flatten

    Returns:
        Iterable[int]: Flattened array
    """
    l = []
    for e in array:
        if isinstance(e, list):
            l += flat_list(e)
        else:
            l.append(e)
    return l
