# Zadanie 3.3 | Operacje na listach
#
# Przygotuj funkcję, która będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
#
# - `suma(liczby)` - zwraca sumę liczb z listy `liczby`
# - `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
# - `max(liczby)` – zwraca największą wartość z listy `liczby`
# - `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
# - `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
# - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
# - `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `ile_wiekszych(tab, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
# 1
liczby = [23,56,43,87,45,65,78]
def suma(liczby):
    a = 0
    for x in liczby:
        a += x
    return a
print(suma(liczby))
# 2
def srednia(liczby):
    a = 0
    for x in liczby:
        a += x
    return (a / len(liczby))
print(srednia(liczby))
# 3 max(liczby)` – zwraca największą wartość z listy `liczby`
def max(liczby):
    a=0
    for x in liczby:
        if x > a:
            a = x
        else:
            continue
    return a
print(max(liczby))
# 4 roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
def roznica_min_max(liczby):
    a = 0
    for x in liczby:
        if x > a:
            a = x
        else:
            continue
    b = liczby[0]
    for i in liczby:
        if i < b:
            b = i
        else:
            continue
    return (a - b)
print(roznica_min_max(liczby))
# 5 - `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
def wypisz_wieksze(liczby, x):
    lista_1 = list()
    for i in liczby:
        if i > x:
            lista_1.append(i)
        else:
            continue
    return print(lista_1)
wypisz_wieksze(liczby,40)
# 6 - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
def pierwsza_wieksza(liczby, x):
    for i in liczby:
        if i > x:
            return i
        else:
            continue
        return None
print(pierwsza_wieksza(liczby, 90))
# 7 - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
def suma_wiekszych(liczby, x):
    lista_1 = list()
    for i in liczby:
        if i > x:
            lista_1.append(i)
        else:
            continue
    return sum(lista_1)
print(suma_wiekszych(liczby,70))
# 8 - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
def ile_wiekszych(liczby, x):
    lista_1 = list()
    for i in liczby:
        if i > x:
            lista_1.append(i)
        else:
            continue
    return len(lista_1)
print(ile_wiekszych(liczby, 70))
# 9 - `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
def wypisz_podzielne(liczby, x):
    lista_2 = list()
    for i in liczby:
        if i % x == 0:
            lista_2.append(i)
        else:
            continue
        return print(lista_2)
wypisz_wieksze(liczby,44)
# 10 - `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma

# 11 - `ile_wiekszych(tab, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`

# 12 - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
def znajdz_wspolny(liczby1, liczby2):
    return (liczby1 & liczby2)