from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    L = sorted(data)
    duplicates = set()
    result = data.copy()
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i] == L[j]:
                duplicates.add(L[i])
    print("duplicates: " + str(duplicates))
    unique = set(L) - duplicates
    print("unique: " + str(unique))
    for e in data:
        if e in unique:
            result.remove(e)
    print("result: " + str(result))
    return result