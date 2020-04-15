# ## Zadanie 1.6 | Bilety (ok. 1 godz.)
#
# Założenia:
# 	- 0-6   - wiek przedszkolny - cena biletu: 0
# 	- 7-17  - wiek szkolny      - cena biletu: 2.28
# 	- 18-64 - wiek dorosły      - cena biletu: 3.80
# 	- +65   - wiek emerytalny   - cena biletu: 1.90
#
# Napisz program, który przyjmuje dwie informacje:
# jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
#
# Na tej podstawie i powyższych założeń policz ile zapłaci za bilety,
# które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.


wiek = int(input("Podaj wiek osoby kupującej: "))
bilety = int(input("Podaj liczbę biletów: "))


if 0 <= wiek <= 6:
    cena = 0
elif 7 >= wiek <= 17:
    cena = 2.28
elif 18 >= wiek <= 64:
    cena = 3.80
elif wiek >= 65:
    cena = 1.90
print(f"Za bilety musisz zapłacić: {cena * bilety} PLN")

#Dlaczego nie dziala np. dla wieku 25, 32?
