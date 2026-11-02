"""načítavaj čísla dovtedy, pokiaľ nenačítaš číslo väčšie ako 100. Ak sa to stane,
 program skončí a vypíše celkový počet načítaných číse"""
pocet = 0

while True:
    cislo = int(input("Zadaj číslo: "))
    pocet += 1
    if cislo > 100:
        break
print("Celkový počet načítaných čísel je:", pocet)

"""načítavaj čísla dovtedy, pokiaľ ich súčet nepresiahne hodnotu 100.
 Program vypíše hodnotu tohto súčtu a aj počet čísel"""
pocet=0
sucet=0
while sucet < 100:
    cislo = int(input("Zadaj číslo: "))
    pocet +=1
    sucet += cislo
    if cislo > 100:
        break
print("Počet čisel je ", pocet)
print("Súčet čisel je ", sucet)

"""napíš program, ktorý bude načítavať čísla dovtedy pokiiaľ nezadáte nulu.
 Na záver program vypíše aritmetický priemer týchto čísel. Nulu do priemeru nezahrňte"""
sucet = 0
pocet = 0
while True:
    cislo = int(input("Zadaj číslo: "))
    if cislo == 0:
        break
    sucet += cislo
    pocet += 1
if pocet > 0:
    aritmeticky_priemer = sucet / pocet
    print("Aritmetický priemer je:", aritmeticky_priemer)



