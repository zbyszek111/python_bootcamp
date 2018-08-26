def czy_jest_pierwsza(n):
    for dzielnik in range(2, n):
        if n % dzielnik == 0:
            return False
        else:
            return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(3)
    assert czy_jest_pierwsza(7)

def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert not czy_jest_pierwsza(4)