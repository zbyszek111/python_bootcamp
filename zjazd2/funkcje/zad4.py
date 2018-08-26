def formatuj(*napisy, **znaczniki):
    napisy = "\n".join(napisy)
    for znacznik in znaczniki:
        napisy = napisy.replace(f"${znacznik}", str(znaczniki[znacznik]))
    return napisy



def test_formatuj_napis_bez_znacznikow():
    assert formatuj("Hello World") == "Hello World"

def test_formatuj_wiele_napis_bez_znacznikow():
    assert formatuj("Hello World","Hello world")== "Hello World\nHello world"

def test_formatuj_napis_z_znacznikiem():
    assert formatuj('koszt $cena PLN','kwota $cena brutto', cena =10)== "koszt $10 PLN'\nkwota $10 brutto"