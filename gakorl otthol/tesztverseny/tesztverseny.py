valaszok = []

f = open("valaszok.txt")
adatok = f.read().split("\n")[:-1]   
f.close()

helyes = adatok[0]
adatok.remove(helyes)

for e in adatok:
    valaszok.append(e.split(" "))
    
print(f"2. feladat: A vetélkedőn {len(adatok)} versenyző indult.")
print("3 feladat: ")
beker = input("A versenyzo azonositoja.")

for e in valaszok:
    if e[0] == beker:
        print(f"{e[1]}\t (a versenyzo valasza)")
        versenyzovalasza = e[1]
      
print("4. feladat: ")
print(f"{helyes}\t (a helyes megodas)")
print(versenyzovalasza)

for e,betu in enumerate (versenyzovalasza):
	# print(sorszam, betu)
	if betu == helyes[e]:
		print("+", end = "")
	else:
		print("-",end = "")
			
		
db = 0		
print("\n 5. feladat: ")
sorszam = int(input("A feladat sorszama: "))
for e in valaszok:
	if e[1][sorszam] == helyes[sorszam]:
		db += 1
print(f"A feladatara {db} fo, a versenyzok {len(valaszok)/db*10} szazaleka adott helyes valaszt.")
