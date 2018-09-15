from zjazd4.mathematica.mathematica.geometry import figures


def test_square_area():
    assert figures.square_area(3, 3) == 9

def test_triangle():
    assert figures.triangle_area(1,2)==1