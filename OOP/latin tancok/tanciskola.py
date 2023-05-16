class tanc:
    def __init__(self, tanc, lany, fiu):
        self.tanc = tanc
        self.lany = lany
        self.fiu = fiu
    def __str__(self):
        return f"tanc: {self.tanc}, lany: {self.lany}, fiu:, {self.fiu}"
    def isVilma(self):
        return self.lany == "Vilma"

sorok = []
#2. megoldas:
f = open("tancrend.txt")
tancok2 = []
temp = []
for e in f:
    sorok.append(e.strip())
    #2. megoldas
    if len(temp) < 3:
        temp.append(e)
    else:
        tancok2.append(tanc(temp[0],temp[1], temp[2]))
f.close()

#print(sorok)

#1. megoldas:
tancok = []
for e in range(len(sorok)//3):
    tancnev=sorok[e*3]
    lany=sorok[e*3+1]
    fiu=sorok[e*3+2]
    tancok.append(tanc(tancnev, lany, fiu))
print(tancok)

print("2. feladat: ")

print(f"elso tanc: {tancok[0].tanc}, utolso tanc: {tancok[-1].tanc}")

db = 0

for egytanc in tancok:
    if egytanc.tanc == "samba":
        db += 1

print(f"Ennyi szamba volt: {db}")

print("Vilma ezekben szerepelt: ")
for egytanc in tancok:
    if egytanc.isVilma():
        print(egytanc.tanc)






