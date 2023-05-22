f=open("felszam.txt","r")
valaszok = []
kerdesek=[]
for sor in f:
    josor = sor.replace("\n","")
    josor2=f.readline().replace("\n","").split(" ")
    #print(josor2)
    valaszok.append(josor2)
    kerdesek.append(josor)
# print(len(kerdesek))
#print(valaszok)
f.close()
print("2. Feladat: ")
print(f"Az adatlapban {len(kerdesek)} kerdes van.")
print("3. Feladat: ")
matekpontok = []
matek = 0
for e in valaszok:
    #print(e)
    if e[2] == "matematika":
        matek += 1
        matekpontok.append(e)
    
print(f"Az adatfájlban {matek} matek feladat van.")    
print(matekpontok)
egypont = 1
ketpont = 1
harompont = 1
egy = 1
ketto = 2
harom = 3
for e in matekpontok:
    print(e[1])
    if e[1] == egy:
        egypont += 1
    elif e[1] == ketto:
        ketpont += 1
    elif e[1] == harom:
        harompont += 1
print(f"1 pontot er {egypont} feladat, 2 pontot er {ketpont} feladat, 3 pontot er {harompont} feladat")
