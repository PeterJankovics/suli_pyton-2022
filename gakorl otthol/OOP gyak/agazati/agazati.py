class Triatlon:
    def __init__(self, nev, nem, szul, uszas, kerekp, futas, rajtszam):
        self.nev = nev
        self.nem = nem
        self.szul = szul
        self.uszas = uszas
        self.kerekp = kerekp
        self.futas = futas
        self.rajtszam = rajtszam

f = open("triatlon.txt","r")
adatok = []
for szam,e in enumerate(f):
    if szam != 0:
        temp = e.strip().split(";")
        adatok.append(Triatlon(*temp))
f.close()
#print(adatok)
print("2. Feladat: ")
print(len(adatok))
