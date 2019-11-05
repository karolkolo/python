import random

liczba_jeden = random.randint(0, 99)
liczba_dwa = random.randint(0, 99)

suma = int(liczba_jeden + liczba_dwa)

while True:

    print(f"Wartosc liczby pierwszej wynosi {liczba_jeden}, wartosc liczby drugiej wynosi {liczba_dwa}")
    odpowiedz = int(input("Jaka jest suma podanych liczb?: "))

    if odpowiedz == suma:
        print("Dobra odpowiedz")
        break
    else:
        print("Odpowiedz jeszcze raz")