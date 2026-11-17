#1. Vytvor prázdny zoznam nakup. Pomocou cyklu for načítaj od používateľa 5 produktov.
# Každý produkt pridaj do zoznamu metódou append(). Na konci vypíš celý nákupný zoznam
#a počet produktov.
nakup=[]
for i in range(5):
    potraviny=input("Nakup: ")
    nakup.append(potraviny)
print(nakup, len(nakup))

#2. Vytvor prázdny zoznam teploty. Pomocou cyklu for načítaj 5 teplôt od používateľa a
# ulož ich do zoznamu pomocou append(). Vypíš zoznam, najvyššiu a najnižšiu teplotu a
# vypočítaj priemernú teplotu.
teploty=[]
for i in range(5):
    teplota=int(input("Teplota: "))
    teploty.append(teplota)
print(teplota,"Najviššia teplota je: " max(teplota), min(teplota), sum(teplota)/len(teplota))