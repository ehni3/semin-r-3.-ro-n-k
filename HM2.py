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

"""napíš program, ktorý bude v cykle načítavať slová dovtedy, pokiaľ nezadáte slovo začínajúce sa na
 písmeno "x". Program vypíše celkový počet znakov všetkých slov okrem posledného slova, 
 začínajúceho sa na x  """

pocet = 0
slovo = input("Zadaj slovo: ")

while slovo[0] != "x":
    pocet = pocet + len(slovo)
    slovo = input("Zadaj slovo: ")

print("Celkový počet znakov je:", pocet)
