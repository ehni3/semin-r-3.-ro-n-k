"""znamky=[1,2,3,4,5]
print(zna
ovocie=["jablko", "broskyňa", "banán", "kaki", "mango"]
print(ovocie[3])
print(ovocie[-2])

print(ovocie[1:4]"""

#Úloha 1) Vytvor zoznam cisla, ktorý bude obsahovať hodnoty 5, 10, 15, 20, 25.
#Vypíš celý zoznam, jeho prvý ,posledný a predposledný prvok.
hodnoty = [5,10,15,20,25]
print(hodnoty, hodnoty[0], hodnoty[4], hodnoty[3])

#Úloha 2 ) Máme zoznam:
#farby = ["cervena", "modra", "zelena"]
#Zmeň druhý prvok na "zlta" a vypíš upravený zoznam.
farby = ["cervena", "modra", "zelena"]
print(farby[0], "žltá", farby[2])

#Úloha 3 ) Vytvor zoznam mena s tromi menami. Pridaj štvrté meno pomocou append(),
#odstráň jedno meno pomocou remove() a vypíš počet zostávajúcich prvkov.
mena= ["jano", "fero", "lubo"]
mena.remove("fero")
mena.append("samo")
print(mena)

#Úloha 1) Vytvor zoznam cisla = [3, 6, 9, 12, 15] a pomocou cyklu for vypíš všetky
#jeho prvky, každý na samostatný riadok.
cisla = [3, 6, 9, 12, 15]

#For cyklus
cislo=[5,10,15,20,25]
for i in cislo:
    print(i)
for cis in range(len(cislo)):
    print(cislo[cis])

cisla=[12,725,3,25,95,31]
for i in cisla:
    print(i)

for z in range(len(cisla)):
    print(cisla[z])

h=0
while h<len(cisla):
    print(cisla[h])
    h+=1

#vytváranie zoznamu pomocou for + metoda appent()
znamky=[]
for i in range(5):
    znamka=int(input("Zadaj známku: "))
    znamky.append(znamka)
print("Znamky sú ", znamky)
print("Priemer: ",sum(znamky)/len(znamky))

#vytvorenie zoznamu pomocou list comprehencia
z=[int(input("Zadaj známku: ")) for i in range(5)]
print(z)