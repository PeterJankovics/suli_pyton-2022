class telek:
    paros = False
    szelesseg = 0
    kerites = ""
    hazszam = 0
    def __init__(self, sor, hazszam):
        #sor: "1 8 k"
        vag = sor.replace("\n","").split(" ")
        #print(vag)
        if vag[0] == 1:
            paros = False
        else:
            paros = True
        #szebb megoldas:
        self.paros = vag[0] == 0
        self.szelesseg = int(vag[1])
        self.kerites = vag[2]
        if self.paros:
            self.hazszam = hazszam[-1]*2
        else:
            self.hazszam = hazszam[0]*2-1
#t = telek("1 8 k")

telkek = []
f = open("kerites.txt")
db = 0
for e in f:
    telkek.append(telek(e, [len(telkek)-paros,paros]))
    if telkek[-1].paros:
        db += 1

f.close()
#print(telkek[-1].kerites)

print("2. Feladat:")
print(f"Az eladott telkek szama {len(telkek)}.")

print("3. Feladat:")

if telkek[-1].paros:
    print("A paros oldalon adták el az utolso telket.")
else:
    print("A paratlan oldalon adták el az utolso telket.")
    
