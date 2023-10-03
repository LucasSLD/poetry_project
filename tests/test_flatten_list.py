from poetry_project.flatten_list import flat_list

def test_flatten_list():
    assert list(flat_list([1, 2, 3])) == [1, 2, 3]
    assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
    assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
        2,
        4,
        5,
        6,
        6,
        6,
        6,
        6,
        7,
    ]
    assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]