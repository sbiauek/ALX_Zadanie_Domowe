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


#########6



import math

def pole_trojkata(bok_a: int, bok_b: int, bok_c: int) -> int:
    return math.sqrt(p * ((p - bok_a) * (p - bok_b) * (p - bok_c)))

print("Podaj długość boków trójkąta.")
bok_a = int(input("Bok A: "))
bok_b = int(input("Bok B: "))
bok_c = int(input("Bok C: "))

p = (bok_a + bok_b + bok_c) / 2
pole = pole_trojkata(bok_a, bok_b, bok_c)
if bok_a + bok_b < bok_c or bok_b + bok_c < bok_a or bok_a + bok_c < bok_b:
    print("Z takich boków nie da się zbudować trójkąta")
else:
    print(f"Pole trójkąta wynosi: {round(pole, 2)} cm2 ")

def test_pole_trojkata():
    assert pole_trojkata(5, 5 ,5) == 10.83

