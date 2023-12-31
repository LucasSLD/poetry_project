from poetry_project.non_unique_elements import checkio


def test_non_unique_elements():
    """Test checkio() function"""
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
    assert not list(checkio([1, 2, 3, 4, 5]))
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
    assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
    assert list(checkio([10, 20, 30, 10])) == [10, 10]
    assert not list(checkio([7]))
    assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
    assert list(checkio([99, 98, 99])) == [99, 99]
    assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
    assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]
