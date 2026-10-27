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

"""number=int(input("Zadaj číslo: "))
sucet=0
moc_des=1
while number > 0:
    cifra=number%3
    sucet= sucet + (cifra*moc_des)
    number//=3
    moc_des*=10
print("Číslo vo dvojkovej sústave ", sucet)"""

"""number=int(input("Zadaj číslo: "))
sucet=0
moc_des=1
while number > 0:
    cifra=number%10
    sucet= sucet + (cifra*moc_des)
    number//=10
    moc_des*=2
print("Číslo vo dvojkovej sústave ", sucet)"""

"""number = int(input("Zadaj číslo: "))
delitel = 2
while number > 1:
    if number % delitel == 0:
        print(delitel, end=",")
        number = number // delitel
    else:
        delitel +=1"""

number = int(input("Zadaj číslo: "))
delitel = 0
for i in range(2, int(number**0.5)):
    if number % 1 ==0:
        delitel +=1
        print("Nie je to prvočíslo")
        break
if delitel == 0:
    print("Je to prvočíslo.")
