import math

######
#Stwórz następujące metody. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

#1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
#2. `max` - zwraca większą z dwóch liczb,
#3. `srednia` - oblicza średnią z dwóch liczb,
#4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
#podpowiedź: wartość PI jest dostępna jako `Math.PI`
#5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
#6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
#7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
#8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

#Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.
######
# 1
def stopny_na_metry(a):
    return a*0.3048
# 2
def max(a,b):
    if a > b:
        return a
    else:
        return b
print(max(3,5))

# 3
def srednia(a,b):
    return (a + b)/2

# 4
def pole_kola(r):
    return int(math.pi * (r**2))
print(f"pole kola wynosi: {pole_kola(5)}")
# 5
def bmi(h,w):
    return (w / (h**2))

# 6
def pole_trojkata(a,b,c):
    p = int((a + b + c) / 2)  # polowa obwodu trojkata
    return  math.sqrt(int(p * (p - a) * (p - b) * (p - c)))


print((f"Pole trojkata wynosi {int(pole_trojkata(4,5,6))}"))
# 7
def kilometry_na_mile(a):
    return a * 0.62

# 8
def mile_na_kilometry(a):
    return a * 1.609
