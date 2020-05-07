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


import calendar

def liczba_dni_w_miesiacu(rok: int, miesiac: str) -> int:
        return calendar.monthrange(rok, miesiac)[1]

rok = int(input("Choose a year: "))
miesiac = int(input("Choose a month (number): "))
nazwa = calendar.month_name[miesiac]


print(f"{nazwa}, {rok} has {liczba_dni_w_miesiacu(rok, miesiac)} days.")


