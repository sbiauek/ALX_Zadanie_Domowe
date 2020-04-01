# ### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)
#
# Napisz program, który prosi użytkownika (przez `input()`),
# żeby podał, ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli,
# ile trzeba będzie zapłacić za pięć kilo ziemniaków.

cena_ziemniakow = int(input("Podaj cenę kilograma ziemniaków: "))
piec_kilo = cena_ziemniakow * 5
print(f"Cena za pięć kilogramów ziemniaków to {piec_kilo}")
print()
print()
print()
print()

#
# Potem napisz program, który prosi użytkownika (przez `input()`),
# żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
# ile trzeba będzie zapłacić za te ziemniaki.
#
cena_ziemniakow1 = int(input("Podaj cenę kilograma ziemniaków: "))
ile_kilo1 = int(input("Ile kilogramów chcesz kupić: "))
kwota_do_zaplaty = cena_ziemniakow1 * ile_kilo1
print(f"Kwota do zapłaty to {kwota_do_zaplaty}")

# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile
# kilo bananów chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i
# banany razem. I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
print()
print()
print()
print()

cena_ziemniakow2 = int(input("Podaj cenę kilograma ziemniaków: "))
ile_kilo2 = int(input("Ile kilogramów ziemniaków chcesz kupić: "))
cena_bananow = int(input("Podaj cenę kilograma bananów: "))
ile_kilo3 = int(input("Ile kilogramów bananów chcesz kupić: "))
kwota_do_zaplaty3 = cena_ziemniakow2 * ile_kilo2 + cena_bananow * ile_kilo3
print(f"Kwota do zapłaty to {kwota_do_zaplaty3}")