"""number=int(input("Zadaj číslo: "))
sucet=0
while number > 0:
    cifra=number%10
    sucet+=cifra
    number//=10
print("Sučet čisel je ", sucet)"""

"""number=int(input("Zadaj číslo: "))
sucet=0
while number > 0:
    cifra=number%10
    if cifra % 2 == 0:
        sucet+=cifra
    number//=10
print("Súčet párnych cifier je ", sucet)"""

number=int(input("Zadaj číslo: "))
sucet=0
moc_des=1
while number > 0:
    cifra=number%3
    sucet= sucet + (cifra*moc_des)
    number//=3
    moc_des*=10
print("Číslo vo dvojkovej sústave ", sucet)