# ### Zadanie 3.2 | Miesiące
#
# Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
#
# Logikę obliczania liczby dni wydziel do osobnej funkcji.
#
# **Wersja A**
# Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
#
# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.




#A

from calendar import monthrange


def liczba_dni_w_miesiacu(rok: int, miesiac: str) -> int:
        return monthrange(rok, miesiac)[1]

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))


print(f"Ten miesiąc ma {liczba_dni_w_miesiacu(rok, miesiac)} dni")

