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
#print(tancok)

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



tancnev = input("kerek egy tancnevet: ")

for e in tancok:
    if e.lany == "Vilma" and e.tanc == tancnev:
        print(f"A {tancnev} bemutatóján Vilma párja {e.fiu} volt.")
        break
else:
    print(f"Vilma nem táncolt {tancnev}-t.")
        

fiu = []
lany = []

for egytanc in tancok:
    if egytanc.fiu not in fiu:
        fiu.append(egytanc.fiu)
    if egytanc.lany not in lany:
        lany.append(egytanc.lany)
        

#print(", ".join(fiu))
#print(", ".join(lany))

f = open("szereplok.txt","w")
f.write("Lanyok" + ", ".join(lany) + "\n" + ", ".join(fiu))

f.close()

statfiu = {}
statlany = {}

for e in fiu:
    statfiu[e] = 0
for egytanc in tancok:
    statfiu[egytanc.fiu] += 1

for e in lany:
    statlany[e] = 0
for egytanc in tancok:
    statlany[egytanc.lany] += 1

print(statfiu)
print(statlany)









