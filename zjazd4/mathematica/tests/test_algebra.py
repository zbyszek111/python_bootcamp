from zjazd4.mathematica.mathematica.algebra import matrices


def test_add_matrices():
    m1 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    m2 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert matrices.add_matrices(m1, m2) == [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]


def test_sub_matrices():
    m1 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    m2 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert matrices.sub_matrices(m1, m2) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
