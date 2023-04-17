# feladat 1:
beker = input("Kerek egy szot: ")
mgh = ["e","e","u","i","o","a"]
van = 0
for e in mgh:
    if e in beker:
        van = 1

if van == 1:
    print("van benne")
else:
    print("Nincs benne")
        
# feladat 2:
szo = []
f = open("szoveg.txt")
for e in f:
    szo.append(e.strip())
f.close()
