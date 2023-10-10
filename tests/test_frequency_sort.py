from poetry_project.frequency_sort import frequency_sort


def test_frequency_sort():
    """Test"""
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
        4,
        4,
        4,
        4,
        2,
        2,
        2,
        6,
        6,
    ]
    assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
        "bob",
        "bob",
        "bob",
        "carl",
        "alex",
    ]
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
