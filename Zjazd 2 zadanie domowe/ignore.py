# ## 3. Funkcje
#
# Przy pisaniu wszystkich funkcji pamiętaj o `type-hinting`, `docstring` i stworzeniu
# testów do weryfikacji czy funkcja działa poprawnie.
#
# ### Zadanie 3.1 Funkcje liczbowe
#
# Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
#
# 1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
# 2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
# 3. `srednia` - oblicza średnią z dwóch liczb,
# 4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
# podpowiedź: wartość PI jest dostępna jako `Math.PI`
# 5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
# 6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
# 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
# 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
#
# Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.


#1111111111

def stopy_na_metry(stopy: int) -> int:
    """Funkcja przeliczająca stopy na metry"""
    return stopy / 3.2808
stopy = int(input("Podaj liczbę stóp: "))
wynik = (round(stopy_na_metry(stopy), 2))

print(wynik)

def test_stopy_na_metry():
    assert ("25") == 7.62

print("="*30)
#2222222222

def wieksza_liczba(a: int, b: int) -> int:
    """Funkcja zwracająca większą liczbę"""
    if a > b:
        return a

    return b
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
wynik2 = wieksza_liczba(a, b)
print(f"Większa liczba to: {wynik2}")


def test_wieksza_liczba():
    assert (2, 7) == 7

print("="*30)

#3333333333333333

def srednia(a: int, b: int) -> int:
    """Funkcja zwracająca średnią z dwóch liczb"""
    return (a1+b2)/2
a1 = int(input("Podaj liczbę a: "))
b2 = int(input("Podaj liczbę b: "))
wynik3 = srednia(a1, b2)
print(f"Średnia z dwóch podanych liczb to: {wynik3}")


def test_srednia():
    assert (4,10) == 7

print("="*30)
#44444444444

import math

def pole_kola(r: int) -> int:
    """Funkcja obliczająca pole koła na podstawie podanego promienia"""
    return math.pi * r**2

r = int(input("Podaj promień koła: "))
pole = pole_kola(r)
print(f"Pole koła wynosi: {round(pole, 2)}")

def test_pole_kola():
    assert (3) == 28.27

print("="*30)
#55555555555
def bmi (wzrost: float, waga: int) -> int:
  return waga / (wzrost ** 2)


wzrost = float(input("Podaj swój wzrost w metrach: "))
waga = int(input("Podaj swoją wagę w kg: "))

wynik_bmi = bmi(wzrost, waga)
if wynik_bmi < 18.5:
    print(f"Twoje BMI wynosi: {round(wynik_bmi, 2)}. Masz niedowagę")
elif 18.5 <= wynik_bmi <= 24.9:
    print(f"Twoje BMI wynosi: {round(wynik_bmi, 2)}. Twoja waga jest prawidłowa.")
elif 25 <= wwynik_bmi <= 29.9:
    print(f"Twoje BMI wynosi: {round(wynik_bmi, 2)}. Masz nadwagę.")
elif wynik_bmi > 30:
    print(f"Twoje BMI wynosi: {round(wynik_bmi, 2)}. Cierpisz na otyłość. Zgłoś się do swojego lekarza rodzinnego.")

def test_