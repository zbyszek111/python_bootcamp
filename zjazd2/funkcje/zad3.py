def policz_znaki(napis, start ="<", end =">"):
    ile_znakow = 0
    poziom = 0
    for litera in napis:
        if litera == start:
            poziom +=1
           # continue
        elif litera == end:
            poziom -= 1
        elif poziom > 0:
            ile_znakow += poziom

    return ile_znakow


def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0

def test_policz_znaki_z_nawiasami_jeden_poziom():
    assert policz_znaki("Ala <ma> kota") == 2
    assert policz_znaki("Ala <ma ko>ta") == 5
    assert policz_znaki("a<a<a<a>>>") == 6


def test_policz_znaki_zpodanymi_parametrami():
    assert policz_znaki('ala [kota [a kot]] ma [ale]','[',']') == 18












