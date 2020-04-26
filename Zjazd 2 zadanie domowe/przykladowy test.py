# Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.
# Przykład użycia:
# >>> czy_jest_pierwsza(10)
# False
# >>> czy_jest_pierwsza(17)
# True

# Liczba pierwsza
# - bedzie intem
# - wieksza od 1
# - dzieli sie tylko przez 1 i przez sama siebie

def czy_jest_pierwsza(liczba):
    if liczba <= 1:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True


def test_czy_jest_pierwsza():
    liczba = 5
    wynik = czy_jest_pierwsza(liczba)
    assert wynik == True

def test_czy_liczba_nie_jest_pierwsza():
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(6) == False
    assert czy_jest_pierwsza(9) == False
    assert czy_jest_pierwsza(12) == False

def test_przyklady_na_liczby_pierwsze():
    assert czy_jest_pierwsza(5) == True
    assert czy_jest_pierwsza(5) is True
    assert czy_jest_pierwsza(5)

def test_przyklady_na_liczby_nie_pierwsze():
    assert czy_jest_pierwsza(9) == False
    assert czy_jest_pierwsza(9) is False
    assert not czy_jest_pierwsza(9)

# TODO: Przerobić testy tak, żeby przetestować więcej wartości, wziętych z wikipedii

def test_wiele_liczb_pierwszych():
    liczby = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for liczba in liczby:
        assert czy_jest_pierwsza(liczba)


def test_wiele_liczb_nie_pierwszych():
    liczby = [-100, -10, -1, 0, 1, 4, 8, 9, 12, 30, 50, 100]
    for liczba in liczby:
        assert not czy_jest_pierwsza(liczba)