f = open("snooker.txt")
adatok = []
for e in f:
    temp = e.replace("\n","").split(";")
    adatok.append(temp)
f.close()

mezonevek = []
mezonevek.append(adatok[0])
adatok.remove(adatok[0])

print("3. Feladat: ")
print(f"A világranglistán {len(adatok)} versenyző szerepel.")

print("4.Feladatok: ")
ossz = 0
maximum = []
for e in adatok:
    #print(max(e[3]))
    bevetel = int(e[3])
    ossz += bevetel
     
print(f"A versenyzők átlagosan {ossz / len(adatok):.2f}")

print("5. Feladat: ")

kina = []   
maxkina = []
for e in adatok:
    if e[2] == "Kína":
        kina.append(e)
        if e == max(maxkina):
            print("dadsadasd")
print(kina)            
maxmax = 0
   
for e in kina:
    maximum = int(e[3])
    maxkina.append(maximum)

