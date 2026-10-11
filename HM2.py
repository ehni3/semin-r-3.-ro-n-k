"""napíš program, ktorý bude načítavať čísla dovtedy pokiaľ
nezadáte nulu. Na záver program vypíše aritmetický priemer
týchto čísel. Nulu do priemeru nezahrňte"""

sucet = 0
pocet = 0

cislo = int(input("Zadaj číslo: "))

while cislo != 0:
    sucet = sucet + cislo
    pocet = pocet + 1
    cislo = int(input("Zadaj číslo: "))

if pocet > 0:
    priemer = sucet / pocet
    print("Aritmetický priemer je:", priemer)