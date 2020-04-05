# ### Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)
# #
# # Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu,
# a program wylicza, ile trzeba zapłacić. Zasady są takie:
# #
# # - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# # - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# # 	- 200 zł za noc, jeśli nocują jedną noc
# # 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# # 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
# # - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
# #
# # Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
# czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.


wiek = int(input("Podaj swój wiek: "))
liczba_nocy = int(input("Podaj liczbę nocy, które spędzisz w hotelu: "))


if wiek < 18:
    print(f"Do zapłaty masz: {liczba_nocy * 100} złotych.") #nieletni
elif 18 >= wiek < 65 and liczba_nocy == 1:
    print(f"Do zapłaty masz: {liczba_nocy * 200} złotych.") #dorosli
elif 18 >= wiek < 65 and 5 > liczba_nocy <= 2:
    print(f"Do zapłaty masz: {liczba_nocy * 180} złotych.")
elif 18 >= wiek < 65 and liczba_nocy > 5:
    print(f"Do zapłaty masz: {liczba_nocy * 150} złotych.")
elif wiek >= 65 and liczba_nocy == 1:
    print(f"Do zapłaty masz: {(liczba_nocy * 200) * 0.9} złotych.") #emeryci
elif wiek >= 65 and 5 > liczba_nocy <= 2:
    print(f"Do zapłaty masz: {(liczba_nocy * 180) * 0.9} złotych.")
elif wiek >= 65 and liczba_nocy > 5:
    print(f"Do zapłaty masz: {(liczba_nocy * 150) * 0.9} złotych.")


