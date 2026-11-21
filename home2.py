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
print("Teploty: ", teploty)
print("Najvyššia telota je: ", max(teploty))
print("Najnižšia teplota je: ", min(teploty))
print("Priemerná teplota je: ", sum(teploty)/len(teploty))

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

# 4. Pomocou list comprehension vytvor zoznam cisla obsahujúci čísla od 1 do 20. Vypíš ho.
cisla=[i for i in range(1,21)]
print(cisla)

# 5. Pomocou list comprehension vytvor zoznam mocniny obsahujúci druhé mocniny čísel
# od 1 do 10. Vypíš ho.
mocniny=[x**2 for x in range(1,11)]
print(mocniny)

# 6. Pomocou list comprehension vytvor zoznam čísel od 1 do 50, ktoré sú deliteľné piatimi.
# Použi podmienku if a výsledok vypíš.
cisla=[i for i in range(1,51) if i % 5 == 0]
print(cisla)

# 7. Pomocou list comprehension načítaj od používateľa 5 známok (celé čísla), ulož ich do
# zoznamu znamky, vypíš zoznam a vypočítaj priemer.
znamky=[int(input("Zadaj známku: ")) for i in range(5)]
print(znamky)
print(sum(znamky)/len(znamky))


