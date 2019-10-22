dzien_tygodnia = int(input(f"podaj w jaki dzien tygodnia oddales buty do naprawy, przyjmij ze: poniedzialek to 1 , wtorek to 2 etc.:  "))
dlugosc_naprawy = int(input("podaj ile bedzie trwala naprawa: "))
gotowe_do_odbioru = dzien_tygodnia + dlugosc_naprawy

if gotowe_do_odbioru == 1:
    print(f"Buty beda gotowe do odbioru w Poniedzialek")
elif gotowe_do_odbioru == 2:
    print(f"Buty beda gotowe do odbioru we Wtorek")
elif gotowe_do_odbioru == 3:
    print(f"Buty beda gotowe do odbioru w Srode")
elif gotowe_do_odbioru == 4:
    print(f"Buty beda gotowe do odbioru w Czwartek")
elif gotowe_do_odbioru == 5:
    print(f"Buty beda gotowe do odbioru w Piatek")
elif gotowe_do_odbioru == 6:
    print(f"Buty beda gotowe do odbioru w Sobote")
else:
    print(f"Buty beda gotowe do odbioru w Niedziele")
