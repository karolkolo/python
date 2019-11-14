### Zadanie 3.2 | Miesiące

#Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.

#Logikę obliczania liczby dni wydziel do osobnej funkcji.

#**Wersja A**
#Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
###

list_31 = ('styczen','marzec','maj', 'lipiec','sierpien','pazdziernik','grudzien')
list_30 = ('kwiecien','czerwiec','wrzesien','listopad')
def miesiac(miesiac):
    if miesiac in list_31:
        return 31
    elif miesiac in list_30:
        return 30
    elif miesiac == 'luty':
        return 28
mies = input(f"podaj miesiac: ")
print(miesiac(mies.lower()))