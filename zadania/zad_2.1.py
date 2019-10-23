
kilo_ziemniakow_koszt = int(input(f"Podaj ile kosztuje kilo ziemniakow: "))
piec_kg_ziemniakow = (kilo_ziemniakow_koszt * 5)
print(f" 5 kg ziemniakow kosztuje {piec_kg_ziemniakow} zł")
ilosc_ziemniakow = int(input(f" Podaj ile kilo ziemniakow chcesz kupic"))
cena_ziemniaki = kilo_ziemniakow_koszt * ilosc_ziemniakow
print(f"Za {ilosc_ziemniakow} kg ziemniakow zaplacisz {cena_ziemniaki} zł")

kilo_bananow = int(input(f"Podaj ile kosztuje kilo bananow: "))
ilosc_bananow = int(input(f" Podaj ile kilo bananow chcesz kupic"))
cena_banany = kilo_bananow * ilosc_bananow
banany_ziemniaki_cena_razem = cena_ziemniaki + cena_banany
print(f"Musisz zaplacic {banany_ziemniaki_cena_razem} zł za ziemniaki i banany razem")

if cena_banany > cena_ziemniaki:
    print("Zaplacisz wiecej za Banany")
elif cena_ziemniaki > cena_banany:
    print("Zaplacisz wiecej za ziemniaki")
else:
    print("Zaplacisz tyle samo za Banany i Ziemniaki")

