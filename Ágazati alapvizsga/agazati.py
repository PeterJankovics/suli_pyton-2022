print("1. feladat")

szoveg = 0
while type(szoveg) != str:
    try:
        szoveg = str(input("Kerek egy szoveget: "))
    except:
        print("Ez nem egy szoveg!!")
szam = ""
while type(szam) != int: 
    try:
        szam = int(input("Kerek egy egesz szamot: "))
    except:
        print("EZ nem egesz szam")
try:    
    print(szoveg[szam -1]*szam)
except:
    print("Nincs ennyi betu!!")
