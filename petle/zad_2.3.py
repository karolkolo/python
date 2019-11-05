# Zadanie 2.3 | Kalkulator
#
# Napisz program, który w pętli prosi o podanie kolejnego działania w formie jedne linii tekstu. Na podstawie dwóch podanych liczb oraz znaku operacji między nimi oblicza wynik działania matematycznego. Ustalmy, że aby zakończyć użytkownik wpisuje słowo koniec.
#
# Obsłuż co najmniej cztery podstawowe działania matematyczne (`+`, `-`, `*`, `/`).

dzialanie = input(f"Podaj dzialanie: ")
cyfra_1 =int(dzialanie[0])
cyfra_2 = int(dzialanie[2])
while True:
    for znak in dzialanie:
        if znak == "+":
            print(f"{(cyfra_1) + (cyfra_2)}")
        elif znak == "-":
            print(f"{(cyfra_1) - (cyfra_2)}")
        elif znak == "*":
            print(f"{(cyfra_1) * (cyfra_2)}")
        elif znak == "/":
            print(f"{(cyfra_1) / (cyfra_2)}")
