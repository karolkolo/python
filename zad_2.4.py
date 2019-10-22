wiek = int(input("Podaj swoj wiek: "))
ilosc_nocy = int(input("Podaj ile nocy spedzisz w hotelu:"))
oplata_za_pobyt = 0
if wiek < 18:
    oplata_za_pobyt = (ilosc_nocy * 100)
    print(f"Zaplacisz za pobyt {oplata_za_pobyt} zł")
elif wiek >= 18:
    if wiek < 65:
        if ilosc_nocy == 1:
            oplata_za_pobyt = (200)
            print(f"Zaplacisz {oplata_za_pobyt}zl za jedna noc.")
        elif 2 <= ilosc_nocy < 5:
            oplata_za_pobyt = (180 * ilosc_nocy)
            print(f"Zaplacisz {oplata_za_pobyt}zł za {ilosc_nocy} nocy.")
        else:
            oplata_za_pobyt = (150 * ilosc_nocy)
            print(f"Zaplacisz {oplata_za_pobyt}zł za {ilosc_nocy} nocy.")
    else:
        if ilosc_nocy == 1:
            oplata_za_pobyt = (200)
            print(f"Zaplacisz {(oplata_za_pobyt)-(oplata_za_pobyt*0.1)}zl za jedna noc.")
        elif 2 <= ilosc_nocy < 5:
            oplata_za_pobyt = (180 * ilosc_nocy)
            print(f"Zaplacisz {(oplata_za_pobyt)-(oplata_za_pobyt*0.1)}zł za {ilosc_nocy} nocy.")
        else:
            oplata_za_pobyt = (150 * ilosc_nocy)
            print(f"Zaplacisz {(oplata_za_pobyt)-(oplata_za_pobyt*0.1)}zł za {ilosc_nocy} nocy.")






