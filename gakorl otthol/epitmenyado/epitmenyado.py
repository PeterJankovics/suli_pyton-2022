def ado(adosav, alapterulet):
    ar = 0
    if adosav == "A":
        ar = elso[0] * alapterulet
    elif adosav == "B":
        ar = elso[1] * alapterulet
    else:
        ar = elso[2] * alapterulet
        if ar >= 10000:
            return ar
        else:
            return 0

    
f = open("utca.txt")
adatok = []
tartalom = f.read().split("\n")[:-1]
f.close()

for e in tartalom:
    adatok.append(e.replace("\n","").split(" "))    
# print(adatok)
print("2. feladat: ")
elso = adatok.pop(0)
print(f"A mintában {len(adatok)} telek talalhato.")

print("3. feladat")
adoszam = input("Egy tulajdonos adószáma: ")
tulajdonok = []
for e in adatok:
    # print(e[0])
    if e[0] == adoszam:
        tulajdonok.append(e)        

if len(tulajdonok) == 0:
    print("Nem szerepel benne.")
else:
    for e in tulajdonok:
        #print(e)
        print(f"{e[1]} utca {e[2]}")


hazakA = [e for e in adatok if e[3] == "A"]
hazakB = [e for e in adatok if e[3] == "B"]
hazakC = [e for e in adatok if e[3] == "C"]
print(hazakA,hazakB,hazakC)

for i in range(len(hazakA)):
    hazakA[i].append

        
