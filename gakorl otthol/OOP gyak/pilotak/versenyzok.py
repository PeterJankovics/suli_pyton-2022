class Pilotak:
    def __init__(self,nev,szul,nemz,rajt):
        self.nev = nev
        self.szul = szul
        self.nemz = nemz
        self.rajt = rajt
    def __repr__(self):
        return f"{self.nev} {self.szul} {self.nemz} {self.rajt}"
    def szuletes(self):
        xd=i.szul.split(".")
        return int(xd[0])

asd = open("pilotak.csv", encoding = "UTF-8")
adatok = []
for szam,e in enumerate(asd):
    if szam != 0:
        e = e.strip().split(";")
        adatok.append(Pilotak(*e))
asd.close()
#print(adatok)
print(f"3. Feladat: {len(adatok)}")


last = ""
for i in adatok:
    last = i.nev
print(f"4. Feladat: {last}")

print("5. Feladat: ")
for i in adatok:
    if i.szuletes() < 1901:
        print(f"{i.nev}: {i.szul}")

lista = []
for e in adatok:
    if e.rajt != "":
        lista.append(e.rajt)
#print(lista)

minimum = min(lista)
asd2 = ""
for e in adatok:
    if str(minimum) == e.rajt:
        asd2 == e.nemz
print(f"{e.nemz}")
        

