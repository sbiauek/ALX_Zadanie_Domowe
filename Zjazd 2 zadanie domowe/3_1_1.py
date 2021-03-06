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

def test_stopy_na_metry():
    stopy_na_metry(25) == 7.62