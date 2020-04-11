### Zadanie 1.9 FizzBuzz

# Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
# dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.


for fizzbuzz in range(101):
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)
