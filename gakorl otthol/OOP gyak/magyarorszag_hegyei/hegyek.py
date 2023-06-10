class hegyek:
    def __init__(self, nev, hegyseg, magassag):
        self.nev = nev
        self.hegyseg = hegyseg
        self.magassag = int(magassag)
    def __repr__(self):
        return f"{self.nev} {self.hegyseg} {self.magassag}"
    def lab(self):
        return self.magassag * 3.280839895

f = open("hegyekMo.txt", encoding = "UTF-8")
adatok = []
for szam, e in enumerate(f):
    if szam != 0:
        temp = e.strip().split(";")
        adatok.append(hegyek(*temp))
f.close()        
#print(adatok)
print(f"3. feladat: Hegycsucsok szama: {len(adatok)}")

magassag = 0
for e in adatok:
    magassag += e.magassag

print(f"A hegycsucsok atlagos magassaga: {magassag / len(adatok)}")

nagy = []
for e in adatok:
    nagy.append(e.magassag)
legnagyobb = max(nagy)
for e in adatok:
    if e.magassag == legnagyobb:
        print(f"""5. Feladat: A legmagasabb hegycsucs adatai:
        Nev: {e.nev}
        Hegyseg: {e.hegyseg}
        Magassag: {e.magassag}""")
                            
b = "Börzsöny"
magassagertek = int(input("6. feladat: Kerek egy magassagot: "))
van = False
for e in adatok:   
        if e.hegyseg == b and magassagertek > e.magassag:
            print(f"\t Nincs {magassagertek}m-nel magasabb hegycsucs a Borzsonyben!")
            break
        else:
            van == True 
if van == True:
    print(f"\t Van {magassagertek}m-nel magasabb hegycsucs a Borzsonyben!")

db = 0 
for e in adatok:
    if e.lab() > 3000:
        db += 1
print(f"7. feladat: 3000 labnal magasabb hegycsucsok szama: {db}")        



        
    


