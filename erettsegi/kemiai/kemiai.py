f = open("felfedezesek.csv")
elemek = []
for e in f:
    elemek.append(e.replace("\n","").split(";"))
    
f.close()

elemek.pop(0)
print(elemek)
print("3. feladat: Elemek szama: {}".format(len(elemek)))
okor = [e for e in elemek if e[0]== "Ókor"]
print("4. feladat: felfedezések száma az ókorban {}".format(len(okor)))
while True:
    vegyjel = input("5. feladat: kérek egy vegyjelet: ").lower()
    if len(vegyjel) < 3 and len(vegyjel)> 0:
        jo = True
        for i in range(len(vegyjel)):
            if not(vegyjel[i] >= "a" and vegyjel[i] <= "z"):
                jo = False
        if jo:
            break
keresett = [e for e in elemek if e[2].lower() == vegyjel]
if keresett == []:
    print("Nincs ilen az elemben.")
else:
    
