f = open("snooker.txt")
adatok = []

for e in f:
    temp = e.replace("\n", "").split(";")
    adatok.append(temp)
f.close()

elso = adatok.pop(0)

print("3. Feladat: ")
print(f"A vilagranglistan {len(adatok)} versenyzo szerepel.")
versenyzok = len(adatok)

print("4. Feladat: ")
nyeremeny = []

for e in adatok:
    nyeremeny.append(int(e[3]))

atlag = sum(nyeremeny) / versenyzok

print(f"A versenyzok atlagosan {atlag:.2f} fontot kerestek")

print("5. Feladat: ")
kina = []
for e in adatok:
    if e[2] == "Kína":
        kina.append(e)        

maximum = []

for e in kina:
    #print(e[3])
    maximum.append(int(e[3]))
#print(maximum)       

maxmax = max(maximum)
print(maxmax)

adat = []
for e in kina:
    #print(e[3])
    if int(e[3]) == 285000:
        adat.append(e)
#print(adat)
forint = (maxmax * 380)
#print(adat)
print(f"""A legjobban kereso kinai versenyzo:
    Helyezes: {adat[0][0]}
    Nev: {adat[0][1]}
    Nyeremeny osszege: {forint} Ft.""")

print("6. feladat: ")
van = 0
for e in adatok:
    if e[2] == "Norvégia":
        van += 1
            
if van == 1:
    print("Van norveg versenyzo. ")
else:
    print("Nincs norveg versenyzo. ")


print("7. Feladat: Statisztika.")

orszagok = []

for e in adatok:
    orszagok.append(e[2])
    orszagok.sort()

#orszagok = orszagokk.sort()
#print(orszagok)
hany = 0    
for e in orszagok:
    hany  

