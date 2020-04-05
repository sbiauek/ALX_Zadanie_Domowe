# ### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
# # #
# # # Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
# oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników,
# proszę znaleźć samodzielnie).


wzrost = float(input("Podaj swój wzrost w metrach: "))
waga = int(input("Podaj swoją wagę w kg: "))

bmi = waga / (wzrost**2)


if bmi < 18.5:
    print(f"Twoje BMI wynosi: {round(bmi, 2)}. Masz niedowagę")
elif 18.5 <= bmi <= 24.9:
    print(f"Twoje BMI wynosi: {round(bmi, 2)}. Twoja waga jest prawidłowa.")
elif 25 <= bmi <= 29.9:
    print(f"Twoje BMI wynosi: {round(bmi, 2)}. Masz nadwagę.")
elif bmi > 30:
    print(f"Twoje BMI wynosi: {round(bmi, 2)}. Cierpisz na otyłość. Zgłoś się do swojego lekarza rodzinnego.")
    