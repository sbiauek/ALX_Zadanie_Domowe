### Zadanie 2.1 | Zagadka matematyczna

# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
# Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
# Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.


import random

pierwsza_liczba = random.randrange(0, 100)
druga_liczba = random.randrange(0, 100)
print(f"Pierwsza liczba to: {pierwsza_liczba}")
print(f"Druga liczba to: {druga_liczba}")
suma = int(input("Podaj sumę powyższych liczb: "))
suma1 = pierwsza_liczba + druga_liczba
while suma == suma1:
    print("Gratulację! To prawidłowy wynik!")
    break
if suma != suma1:
    print(f"Próbuj dalej!") #Nie wiem jak zrobić tutaj, żeby wracało do "PODAJ SUME POWYZSZYCH LICZB
                             #probowalem z continue, ale mi kiepsko to wyszlo







