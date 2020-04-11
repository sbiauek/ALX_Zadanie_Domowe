# ### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
#
# Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
# (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
#
# Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
#
# Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
#
# ```
# import math
#
# x = math.sqrt(10)
# ```
from math import sqrt



print("Podaj długość boków trójkąta.")
bok_a = int(input("Bok A: "))
bok_b = int(input("Bok B: "))
bok_c = int(input("Bok C: "))

p = (bok_a + bok_b + bok_c) / 2

pole_trojkata = sqrt(p * ((p - bok_a) * (p - bok_b) * (p - bok_c)))

if bok_a + bok_b > bok_c:
    print("Z takich boków nie da się zbudować trójkąta")
else:
    print(f"Pole trójkąta wynosi: {pole_trojkata} cm2")

