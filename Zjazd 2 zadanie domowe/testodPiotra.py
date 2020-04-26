def czy_jest_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(3, liczba):
        if liczba % i == 0:
            return False
    return True
def test_czy_jest_pierwsza():
    liczba = 5
    wynik = czy_jest_pierwsza(liczba)
    assert wynik == True