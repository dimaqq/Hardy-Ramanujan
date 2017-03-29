import cubes


def test_int():
    x3 = cubes.Int(3, (1, 2), "foo")
    assert x3 == 3


def test_int_comparison():
    x1 = cubes.Int(1, (1, 1), "a")
    x2 = cubes.Int(2, (9, 9), "z")
    x3 = cubes.Int(3, (3, 3), "b")
    assert x1 < x2 < x3


def test_int_equality():
    assert cubes.Int(123, None, None) == cubes.Int(123, 67, "foo")


def test_int_large():
    x = cubes.Int(3 ** 237, None, None)
    assert x == 3 ** 237


def test_solutions_finds_hardy_ramanujan():
    assert 1729 in list(cubes.solutions(2000))


def test_solutions_discards_identical():
    assert list(cubes.solutions(2000)) == [1729]
