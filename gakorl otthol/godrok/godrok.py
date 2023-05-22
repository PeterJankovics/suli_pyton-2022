bemenet = open("melyseg.txt")
mélységek = []
for sor in bemenet:
    mélységek.append(int(sor.strip()))

print("1. feladat")
print(f'A fájl adatainak száma: {len(mélységek)}')

print("2. feladat")
hely = int(input("Adjon meg egy távolságértéket! "))
print(f'Ezen a helyen a felszín {mélységek[hely - 1]} méter mélyen van.')

print("3. Feladat: ")
erintetlen = 0
for mert in mélységek:
    if mert == 0:
        erintetlen += 1
print("Az erintetlen teruletek aranya {:.2f}".format(erintetlen / len(mélységek) * 100))        

print("4. Feladat: ")

f = open("godrok.txt","w")

f.close()

print("6. Feladat:")

