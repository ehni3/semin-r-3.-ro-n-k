#1. Vytvor prázdny zoznam nakup. Pomocou cyklu for načítaj od používateľa 5 produktov.
# Každý produkt pridaj do zoznamu metódou append(). Na konci vypíš celý nákupný zoznam
#a počet produktov.
"""nakup=[]
for i in range(5):
    potraviny=input("Nakup: ")
    nakup.append(potraviny)
print(nakup, len(nakup))"""

#2. Vytvor prázdny zoznam teploty. Pomocou cyklu for načítaj 5 teplôt od používateľa a
# ulož ich do zoznamu pomocou append(). Vypíš zoznam, najvyššiu a najnižšiu teplotu a
# vypočítaj priemernú teplotu.
"""teploty=[]
for i in range(5):
    teplota=int(input("Teplota: "))
    teploty.append(teplota)
print("Teploty: ", teploty)
print("Najvyššia telota je: ", max(teploty))
print("Najnižšia teplota je: ", min(teploty))
print("Priemerná teplota je: ", sum(teploty)/len(teploty))"""

# 3. Vytvor prázdny zoznam body. Pomocou cyklu for načítaj body 6 žiakov a ulož ich pomocou
# append(). Vypíš zoznam a priemerný počet bodov. Pomocou ďalšieho cyklu for a podmienky
# if zisti, koľko žiakov získalo aspoň 15 bodov.
body=[]
for i in range(6):
    ziak_bod=int(input("Počet bodov žiaka: "))
    body.append(ziak_bod)
print(body)
print("Priemerný počet bodov je:", sum(body)/len(body))
pocet=0
for x in body:
    if x>=15:
        pocet+=1
print("Aspoň 15 bodov ziskalo ",pocet, " žiakov.")


