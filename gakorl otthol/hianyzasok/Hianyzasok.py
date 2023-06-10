f= open("szeptember.csv")
adatok = []
for e in f:
    temp = e.replace("\n","").split(";")
    adatok.append(temp)
f.close()

elso = []

elso.append(adatok[0])
adatok.remove(adatok[0])

#print(elso)

mulasztott = []
for e in adatok:
    mulasztott.append(int(e[4]))
#print(mulasztott)
    
print(f"""2. Feladat:
        osszes mulasztott orak szama: {sum(mulasztott)}""")


print("3. Feladat: ")

szam = int(input("Kerek egy napot (1 es 30 kozott). "))
nev = str(input("Kerek egy tanulo nebvet. "))

if szam and nev not in adatok:
    print("a")
else:
    print("b")
    
