def pontszamit(valasz, helyes):
    pont = 0
    for sorszam, betu in enumerate (valasz):
        if betu == helyes[sorszam]:
            if sorszam < 5:
                pont += 3
            elif sorszam < 10:
                pont += 4
            elif sorszam < 14:
                pont += 5
            else:
                pont += 6
    return pont                        

            
f = open("valaszok.txt","r")
print("1. feladat:")

adatok = f.read().split("\n")[:-1]
f.close()
# print(adatok)

helyes = adatok[0]

adatok.remove(helyes)
valaszok = []

for e in adatok:
    valaszok.append(e.split(" "))
    
# print(valaszok)
print("2. feladat:")
print("A versenyen " + str(len(valaszok)) + " indult")


print("3. feladat: ")


versenyzok = input("A versenyző azonosítója: ")
versenyzovalasza = ""
for e in valaszok:
    if e[0] == versenyzok:
        print(e[1] + "\t(a versenyző válasza)")
        versenyzovalasza = e[1]
          
print("4. feladat: ")
print(helyes + "\t a helyes megoldás")
print(versenyzovalasza)

for sorszam, betu in enumerate (versenyzovalasza):
    #print(betu, sorszam)
    if betu == helyes[sorszam]:
        print("+", end="")
    else:
        print(" ", end="")
        
print("\t a versenyző helyes válaszai")
print("5. feladat:")
feladat = int(input("A feladat sorszáma = "))
db = 0

for e in valaszok:
    if e[1][feladat] == helyes[feladat]:
        db += 1

print("A feladatra {0} fő, a versenyzők {1:.2%}-a adott helyes választ".format(db, db/len(valaszok)))        

f = open("pontok.txt","w")
eredmenyek = []

for e in valaszok:
    pont = pontszamit(e[1],helyes)
    f.write(e[0] + " " + str(pont) + "\n")
    eredmenyek.append([pont, e[0]])    
f.close()



# eredmenyek.sort()
# eredmenyek.reverse()
# print(eredmenyek[:10])
csakpontok = set({})

for e in eredmenyek:
    csakpontok.add(e[0])
    
top3 = list(csakpontok)[-3:]
top3.sort()
top3.reverse()
for sorszam, i in enumerate (top3):
    print(i)
    for e in eredmenyek:
        if e[0] == i:
            print("{}. {} pont {}".format(sorszam, e[1]))
        
#print(list(csakpontok)[-3:])


























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































