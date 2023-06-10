class Eu:
    def __init__(self, orszag, evszam):
        self.orszag = orszag
        self.evszam = evszam
    def csatlakozas(self):
        a = self.evszam
        return int(a[0:4])
    def honap(self):
        a = self.evszam
        return a[5:7]

f = open("EUcsatlakozas.txt")
adatok = []
for e in f:
    temp = e.strip().split(";")
    adatok.append(Eu(*temp))
f.close()
#print(adatok)

csatlakozas = 0
for e in adatok:
    if e.csatlakozas() <= 2018:
        csatlakozas += 1
print(f"3. Feladat: EU tagallamainak szama: {csatlakozas} db")

ketezerhet = 0
for e in adatok:
    if e.csatlakozas() == 2007:
        ketezerhet += 1
print(f"4. Feladat: 2007-ben {ketezerhet} orszag csatlakozott.")

datuma = 0
majus = ""
for e in adatok:
    if e.orszag == "Magyarország":
        datuma = e.evszam
        
print(f"5. feladat: Magyarorszag csatlakozasanak datuma: {datuma}")
for e in adatok:
    if e.honap() == "05":
        print("6. feladat: Majusban volt a csatlakozasa")
        break

adatok=sorted(adatok,key=lambda e:e.evszam)
print("7. feladat: Legutoljára csatlakozott ország: "+adatok[-1].orszag)

evek = []
for e in adatok:
    evek.append(e.csatlakozas())

for e in adatok:
    if e.orszag == evek:
        print("dad")



