def wiecej_niz(napis, liczba_wystapien):
    wynik = set()
    for litera in napis:
        if napis.count(litera) > liczba_wystapien:
            wynik.add(litera)

    return wynik


def test_wiecej_niz_pusty():
    assert wiecej_niz("", 1) == set()


def test_wiecej_niz_napis():
    assert wiecej_niz("aaa", 2) == {'a'}
    assert wiecej_niz("aaa bbb ccc dd", 2) == {'a','b', 'c', ' '}