import random
szamok = []
szam = 0
for i in range(10):
    szam = random.randint(1,1000)
    if szam % 2 == 0:
        print(szam)
    else:
        print(szam, "nem paros.")
    szamok.append(szam)
szamok.sort()
print(szamok)

