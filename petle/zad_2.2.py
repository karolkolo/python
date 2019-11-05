# Zadanie 2.2 | Choinka

#Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać


liczba = input(f"podaj liczbe calkowita: ")
space = " "
block = "*"
for i in range(1, int(liczba)+1):
    print((int(liczba) - i) * space,(i + (i-1)) * block)