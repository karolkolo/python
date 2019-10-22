wiek = int(input("Podaj wiek osoby kupujacej bilety: "))
ilosc_biletow = int(input("Podaj ilosc biletow: "))

suma_za_bilety = 0

if wiek >=7:
    if wiek <= 64:
        if wiek <= 17:
            suma_za_bilety = (ilosc_biletow * 2.28)
            print(f"Za bilety zaplacisz {suma_za_bilety:.2F} zl ")
        else:
            suma_za_bilety = (ilosc_biletow * 3.8)
            print(f"Za bilety zaplacisz {suma_za_bilety} zl ")
    else:
        suma_za_bilety = (ilosc_biletow * 1.9)
        print(f"Za bilety zaplacisz {suma_za_bilety} zl ")
else:
    suma_za_bilety = 0
    print(f"Za bilety zaplacisz {suma_za_bilety} zl ")

