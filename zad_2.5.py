import math


a = int(input("Podaj dlugosc boku a trojkata: "))
b = int(input("Podaj dlugosc boku b trojkata: "))
c = int(input("Podaj dlugosc boku c trojkata: "))
pole = 0
p = ((a + b + c)/ 2) # polowa obwodu trojkata

if (a + b > c) and (b + c > a) and (c + a > b):
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Pole Trojkata wynosi {pole:.2f} cm kwadratowych")

else:
    print("Boki a,b,c nie moga stworzyc trojkata")


