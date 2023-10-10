from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    """
        Finds the non-unique elements in an array
    Args:
        data (list[int]): _description_

    Returns:
        Iterable[int]: _description_
    """
    l = sorted(data)
    duplicates = set()
    result = data.copy()
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                duplicates.add(l[i])
    print("duplicates: " + str(duplicates))
    unique = set(l) - duplicates
    print("unique: " + str(unique))
    for e in data:
        if e in unique:
            result.remove(e)
    print("result: " + str(result))
    return result
