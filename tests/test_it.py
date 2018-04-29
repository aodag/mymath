import mymath


def test_add():
    result = mymath.add(1, 2)
    assert result == 3


def test_sub():
    result = mymath.sub(1, 2)
    assert result == -1
