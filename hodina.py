number=int(input("Zadaj číslo: "))
sucet=0
while number > 0:
    cifra=number%10
    sucet+=cifra
    number//=10
print("Sučet čisel je ", sucet)
