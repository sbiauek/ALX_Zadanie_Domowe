# FUNKCJE

def hello_world():
    print("Hello world!")


hello_world()
hello_world()


def powiedz_czesc(imie, nazwisko):
    print(f'Cześć {imie} {nazwisko}!')


powiedz_czesc("Piotr", "GG")

moje_imie = "Andrzej"
powiedz_czesc(moje_imie, "Kowalski")


# zwracanie wartosci z funkcji

def suma(a, b):
    return a + b # return wychodzi z funkcji i zadna instrukcja ktora po nim jest sie nie wykona

wynik = suma(2, 3)
print(f"Wynik dodawania = {wynik}")

# Jak z funkcji zwrócić kilka wartości na raz?

def suma_mnozenie(a, b):
    wynik_dodawania = a + b
    wynik_mnozenia = a * b
    return wynik_dodawania, wynik_mnozenia


wynik_a, wynik_b = suma_mnozenie(5, 2)
print(wynik_a)
print(wynik_b)

# Dokumentowanie własnego kodu:
# - są to po prostu komentarze
# - type hinting
#   - sugestia jakiego typu powinny być argumenty albo co funkcja zwraca
# - docstring


def iloczyn(a: int, b: int) -> int:
    """
    Iloczyn dwóch liczb
    :param a: pierwsza liczba do mnozenia
    :param b: druga liczba do mnozenia
    :return:
    """
    return a * b


wynik = iloczyn(2, 3)
print(wynik)

wynik = iloczyn(2.5, 4.1)
print(wynik)

######################################################

napis = 'Ala \'ma kota'
print(napis)

napis = "Ala \"ma kota"
print(napis)

# \ - backslash jest znakiem do eskejpowania znaków, czyli odbierania im specjalnego znaczenia znanego z języka
napis = "\\"
print(napis)

######################################################

def opakowywacz(napis, start=">>", end="<<"):
    return start + napis + end


# tutaj mówimy o argumentach na poziomie
# uruchomienia/wywolania funkcji

# wywowałania pozycyjne
print(opakowywacz("Ala ma kota")) # wywowałania pozycyjne
print(opakowywacz("Ala ma kota", "((")) # wywowałania pozycyjne
print(opakowywacz("Ala ma kota", "((", "))")) # wywowałania pozycyjne

# wywowałania nazwane
print(opakowywacz(napis="Ala ma kota", start="((", end="))"))
print(opakowywacz(napis="Ala ma kota", start="(("))
print(opakowywacz(napis="Ala ma kota", end="))"))
print(opakowywacz(napis="Ala ma kota"))

print(opakowywacz(end='\\\\', start="//", napis="Ala ma kota"))

# Możemy mieszać
print(opakowywacz("Ala ma kota", end="{{"))
print("Ala ma kota", end="----")
print("Ala ma kota")
# Jeżeli mieszamy, to najpierw podajemy argumenty pozycyjne a później nazwa
# print(opakowywacz(end="{{", "Ala ma kota")) # Tak nie można, będzie błąd składniowy

print("="*30)

# Jak przekazywać dowolnie wiele argumentów?
print("ala", "Ela", "Pan Tadeusz", [1,2,3], 1, 3.14, False)

# *args - służy do łapania wszystkich argumentów pozycyjnych - dostajemy tupka z tymi argumentami
# **kwargs - służy do łapania wszystkich argumentów nazwanych
def zliczacz(*args, **kwargs):
    print(args)
    print(kwargs)
    print()


zliczacz()
zliczacz(1)
zliczacz(1, 2, 3)
zliczacz("Ala", "Ela", "Ola")
zliczacz("ala", "Ela", "Pan Tadeusz", [1,2,3], 1, 3.14, False)

zliczacz(a=1, b=2, c=3)

zliczacz('ala', 'ela', 'krysia', waga=100, wiek=20, wzrost=500)


# możemy połączyć argumenty pozycyjne, z wartością domyślną i łapacze args i kwargs
def foo(a, b, c=10, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


foo(1, 2, 3, 4, 5, 6, 7, imie="Tomek", wiek=20, wzrost=167)

print("="*100)

# #############################
# Co jest prawdą a co fałszem??
# #############################

# pusty str -> False
# cokolwiek w stringu -> True, nawet '0' albo 'False'
# int 0 -> False, jakakolwiek inna liczba daje True
# kolekcje (list, set, dict, tuple): pusta kolekcja - False, w kolekcji jest jakikolwiek element to True
# None -> False

zmienna = 'Ala ma kota' # T
zmienna = 'A' # T
zmienna = '' # F
zmienna = '0' # T
zmienna = 'False' # T
zmienna = 0 # F
zmienna = 10 # T
zmienna = -5 # T
zmienna = [] # F
zmienna = [0] # T
zmienna = None # F

if zmienna:
    print("PRAWDA")
else:
    print("falsz")

####################################


wynik_z_printa = print("Ala ma kota")

# print nic sensownego nie zwraca,
# przy przypisaniu dostaje None
# w zmiennej wynik_z_printa siedzi None

if print("Ala ma kota"):
    print("prawda")
else:
    print("falsz")

print("="*30)

# leniwe wyliczanie warunku
# or - jeżeli lewa strona jest prawdziwa, to prawa nie jest wyliczana!!
zmienna = 5

if zmienna < 1 or print("Ala ma kota"):
    print("PRAWDA")
else:
    print("FALSZ")

print("="*30)

zmienna = 5
if zmienna < 1 and print("leniwe wyliczanie"):
    print("PRAWDA")
else:
    print("FALSZ")

print("="*30)

##############################################

lista = [1, 2, 3]
print(lista)
# dodać jeden element na koniec listy
lista.append(4)
print(lista)

lista += [5, 6, 7]

print(lista)


print("="*30)

##############################################

# sprawdzanie typu
zmienna = [1, 2, 3]
print(isinstance(zmienna, list)) # True
print(isinstance(zmienna, str)) # False
print(isinstance(zmienna, int)) # False



print("="*30)

##############################################

def kwadrat(x):
    return x ** 2

wynik = kwadrat(3)
print(wynik)
print(type(kwadrat))


kwadrat2 = lambda x: x ** 2

wynik2 = kwadrat2(4)
print(wynik2)
print(type(kwadrat2))


def sumator(a, b, c):
    return a + b + c

print(sumator(10, 20, 30))


sumator2 = lambda a, b, c: a+b+c
print(sumator2(10, 20, 30))


#####################################

funkcja1 = lambda x: x ** 3

wynik = funkcja1(5)
print(wynik)

zmienna2 = funkcja1
wynik = zmienna2(2)
print(wynik)

print("="*30)
#####################################

# lista - to będzie zwykła lista wartości
# operacja - to będzie funkcja lamda
def wykonaj_operacje_na_liscie(lista, operacja):
    wynik = []

    for element in lista:
        wynik.append( operacja(element) )

    return wynik


pomiary = [10, 20, 30, 40, 50]
print(pomiary)
przetworzone_pomiary = wykonaj_operacje_na_liscie(pomiary, lambda x: x**2)
print(przetworzone_pomiary)

print("="*30)

########################################

pomiary = [10, 20, 30, 40, 50]
print(pomiary)

przetworzone_pomiary = list(map(lambda x: x ** 2, pomiary))
print(przetworzone_pomiary)

########################################
wagi_w_kg = (80, 99, 120, 55, 88, 20, 132, 100, 68, 34)
wzrosty_cm = (182, 170, 200, 205, 162, 158, 199, 178, 202, 168)

wzrosty_m = tuple(map(lambda wzrost: wzrost / 100.0, wzrosty_cm))
print(wzrosty_cm)
print(wzrosty_m)

# lista tupli (waga, wzrost)
dane = list(zip(wagi_w_kg, wzrosty_m))
print(dane)

wyniki_bmi = list(map(lambda pomiar: pomiar[0] / pomiar[1] ** 2, dane))
print(wyniki_bmi)

przefiltrowane_bmi = list(filter(lambda bmi: bmi > 15.0, wyniki_bmi))
print(przefiltrowane_bmi)