from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __mul__(self, other):
        new_x = self.x * other
        new_y = self.y * other
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __ne__(self, other):
        return self.length != other.length

    def __le__(self, other):
        return self.length <= other.length

    def __str__(self):
        return f'V({self.x}, {self.y}):{self.length:.2f}'


    @property
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)


def test_create_():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1.x == 1
    assert v1.y == 2


def test_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6


def test_sub():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 - v2
    assert v3.x == -2
    assert v3.y == -2


def test_mul():
    v1 = Vector(1, 2)
    v2 = 4
    v3 = v1 * 4
    assert v3.x == 4
    assert v3.y == 8


def test_len():
    v1 = Vector(3, 4)
    assert v1.length == 5.0


def test_equal():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)
    assert v1 == v2


def test_equal1():
    v1 = Vector(3, 4)
    v2 = Vector(-3, 4)
    assert v1 == v2


def test_equal2():
    v1 = Vector(3, 4)
    v2 = Vector(0, 5)
    assert v1 == v2


def test_grather_than():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    assert v1 > v2

def test_grather_than_or_equal():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    assert v1 >= v2

def test_les_than():
    v1 = Vector(1, 2)
    v2 = Vector(2, 4)
    assert v1 < v2

def test_not_equal():
    v1 = Vector(1, 2)
    v2 = Vector(2, 4)
    assert v1 != v2

def test_les_equal():
    v1 = Vector(1, 2)
    v2 = Vector(2, 4)
    assert v1 <= v2

def test_sort():
    v1 = Vector(1,2)
    v2 = Vector(0,1)
    v3 = Vector(3,2)
    v4 = Vector(0,1)
    lista = [v1,v2,v3,v4]
    assert sorted(lista) == [v4,v2,v1,v3]
    assert sorted(lista) == [v2,v4,v1,v3]

    print(lista)
